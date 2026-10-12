#!/usr/bin/env python3
"""Read-only Markdown navigation/link validator for a local docs vault."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK_START_RE = re.compile(r'(?<!!)\[[^\]\n]*\]\(')
CODE_FENCE_RE = re.compile(r'^ {0,3}(`{3,}|~{3,})(?:[^`~]*)$')
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')
HEADER_RE = re.compile(r'^#{1,6}\s+(.+?)\s*#*\s*$')


def strip_code(text):
    lines = []
    fenced = False
    fence = None
    for line in text.splitlines():
        match = CODE_FENCE_RE.match(line)
        if match:
            mark = match.group(1)
            if not fenced:
                fenced, fence = True, mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fenced, fence = False, None
            lines.append('')
            continue
        lines.append('' if fenced else INLINE_CODE_RE.sub('', line))
    return lines


def links(line):
    """Yield ordinary inline link targets, including balanced parentheses in paths."""
    for match in LINK_START_RE.finditer(line):
        start = match.end()
        if start < len(line) and line[start] == '<':
            end = line.find('>', start + 1)
            if end < 0 or not re.match(r'^\s*(?:"[^"]*")?\)', line[end + 1:]):
                continue
            yield line[start + 1:end]
            continue
        depth = 0
        for pos in range(start, len(line)):
            char = line[pos]
            if char == '(':
                depth += 1
            elif char == ')':
                if depth == 0:
                    target = line[start:pos].strip()
                    # An optional Markdown title follows the target.
                    target = re.sub(r'\s+"[^"]*"$', '', target)
                    if target and not re.search(r'\s', target):
                        yield target
                    break
                depth -= 1


def slugify(s):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s).strip().lower()
    s = re.sub(r'[^\w\- ]', '', s, flags=re.UNICODE)
    return re.sub(r'\s+', '-', s)


def headings(file):
    slugs = set()
    counts = {}
    for line in strip_code(file.read_text(encoding='utf-8')):
        m = HEADER_RE.match(line)
        if m:
            base = slugify(m.group(1))
            n = counts.get(base, 0)
            counts[base] = n + 1
            slugs.add(base if n == 0 else f'{base}-{n}')
    return slugs


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', default='.', help='Git/project root')
    p.add_argument('--vault', default='docs', help='Vault path, relative to project root')
    p.add_argument('--format', choices=['text', 'json'], default='text')
    args = p.parse_args()
    root = Path(args.root).expanduser().resolve()
    vault = (root / args.vault).resolve()
    findings = []
    failed_reads = set()
    def report(severity, code, path, message):
        findings.append(dict(severity=severity, code=code, path=str(path), message=message))

    def safe_headings(path):
        try:
            return headings(path)
        except (OSError, UnicodeError) as exc:
            if path not in failed_reads:
                report('error', 'read_failure', path, str(exc))
                failed_reads.add(path)
            return set()

    if not root.is_dir() or not vault.is_dir() or not vault.is_relative_to(root):
        report('error', 'vault_missing', vault, 'Vault does not exist under project root')
    else:
        home = vault / 'Home.md'
        home_valid = home.is_file() and home.resolve().is_relative_to(root)
        if not home_valid:
            report('error', 'home_missing', home, 'Expected root navigation page Home.md')
        files = sorted(vault.rglob('*.md'))
        if not files:
            report('warning', 'no_markdown', vault, 'Vault contains no Markdown files')
        for file in files:
            if '.obsidian' in file.parts:
                continue
            if not file.resolve().is_relative_to(root):
                report('error', 'outside_root', file, 'Markdown file resolves outside project root')
                continue
            try:
                raw = file.read_text(encoding='utf-8')
            except (OSError, UnicodeError) as exc:
                report('error', 'read_failure', file, str(exc))
                failed_reads.add(file)
                continue
            for line_no, line in enumerate(strip_code(raw), 1):
                for link in links(line):
                    if link.startswith(('#', 'mailto:', 'tel:', 'data:')):
                        if link.startswith('#') and unquote(link[1:]).lower() not in safe_headings(file):
                            report('warning', 'anchor_missing', file, f'Line {line_no}: {link}')
                        continue
                    try:
                        parts = urlsplit(link)
                    except ValueError:
                        report('error', 'link_invalid', file, f'Line {line_no}: {link}')
                        continue
                    if parts.scheme or parts.netloc:
                        continue
                    destination = unquote(parts.path)
                    dest_file = (file.parent / destination).resolve() if destination else file
                    if not dest_file.is_relative_to(root):
                        report('warning', 'outside_root', file, f'Line {line_no}: {link}')
                    elif not dest_file.exists():
                        report('error', 'link_missing', file, f'Line {line_no}: {link}')
                    elif not dest_file.is_file():
                        report('error', 'link_not_file', file, f'Line {line_no}: {link}')
                    elif parts.fragment and dest_file.is_file() and dest_file.suffix.lower() == '.md':
                        if unquote(parts.fragment).lower() not in safe_headings(dest_file):
                            report('warning', 'anchor_missing', file, f'Line {line_no}: {link}')
        if home_valid and len(files) > 1:
            home_links = set()
            try:
                home_lines = strip_code(home.read_text(encoding='utf-8'))
            except (OSError, UnicodeError):
                home_lines = []  # read_failure was already reported above
            for line in home_lines:
                for link in links(line):
                    try:
                        path = urlsplit(link).path
                    except ValueError:
                        continue  # link_invalid was reported in the main scan
                    if path:
                        target = (home.parent / unquote(path)).resolve()
                        if target.is_relative_to(vault) and target.is_file() and target.suffix.lower() == '.md' and target != home:
                            home_links.add(target)
            if not home_links:
                report('warning', 'home_no_valid_links', home, 'Home.md has no valid links to another vault page')
    if args.format == 'json':
        print(json.dumps({'findings': findings, 'errors': sum(f['severity']=='error' for f in findings)}, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{f['severity'].upper()} {f['code']}: {f['path']} — {f['message']}")
        print(f"Results: {sum(f['severity']=='error' for f in findings)} errors, {sum(f['severity']=='warning' for f in findings)} warnings")
    return 1 if any(f['severity'] == 'error' for f in findings) else 0

if __name__ == '__main__':
    sys.exit(main())
