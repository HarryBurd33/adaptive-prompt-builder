#!/usr/bin/env python3
"""Build/check the portable prompt and a deterministic, self-contained skill ZIP."""
import argparse
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'adaptive-prompt-builder'
PORTABLE = ROOT / 'portable' / 'adaptive-prompt-builder.md'
VERSION = '0.1.0'
ARCHIVE = ROOT / 'dist' / f'adaptive-prompt-builder-v{VERSION}.zip'
CHECKSUMS = ROOT / 'dist' / 'SHA256SUMS'


def sources():
    paths = sorted(p for p in SKILL.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in SKILL.rglob('*')):
        raise ValueError('Skill source must not contain symlinks')
    for p in paths:
        if p.suffix == '.md':
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                resolved = (p.parent / target.split('#', 1)[0]).resolve()
                if not resolved.is_relative_to(SKILL.resolve()) or not resolved.is_file():
                    raise ValueError(f'Broken or escaping skill link: {p.name}: {target}')
    return paths


def portable_text():
    text = (SKILL / 'SKILL.md').read_text().split('---', 2)[2].lstrip()
    additions = []
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text):
        label, target = match.groups()
        if '://' not in target and not target.startswith('#'):
            path = SKILL / target
            text_label = f'{label} (included below)'
            additions.append((match.group(0), text_label, path))
    sections = []
    for link, label, path in additions:
        text = text.replace(link, label)
        if path not in [p for p, _ in sections]:
            sections.append((path, path.read_text().strip()))
    notice = (SKILL / 'LICENSE').read_text().strip()
    return ('<!-- Generated from the canonical skill by scripts/package.py. -->\n'
            'Use these instructions to refine my idea into a standalone prompt.\n\n'
            + text.rstrip() + '\n\n'
            + '\n\n'.join('---\n\n' + body for _, body in sections)
            + '\n\n---\n\n## License\n\n' + notice + '\n')


def archive_bytes(paths):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for path in paths:
            info = zipfile.ZipInfo('adaptive-prompt-builder/' + path.relative_to(SKILL).as_posix(),
                                   date_time=(2026, 10, 18, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, path.read_bytes())
    data = output.getvalue()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        if z.testzip() is not None or len(z.namelist()) != len(paths):
            raise ValueError('Archive integrity failure')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without rewriting generated files')
    args = parser.parse_args()
    paths = sources()
    primary = (SKILL / 'SKILL.md').read_text()
    if not primary.startswith('---\n') or 'name: adaptive-prompt-builder\n' not in primary.split('---', 2)[1]:
        raise ValueError('Unexpected skill metadata')
    portable = portable_text().encode()
    archive = archive_bytes(paths)
    checksums = (hashlib.sha256(archive).hexdigest() + '  ' + ARCHIVE.name + '\n'
                 + hashlib.sha256(portable).hexdigest() + '  ../portable/' + PORTABLE.name + '\n').encode()
    expected = {PORTABLE: portable, ARCHIVE: archive, CHECKSUMS: checksums}
    if args.check:
        drift = [str(p.relative_to(ROOT)) for p, data in expected.items()
                 if not p.is_file() or p.read_bytes() != data]
        if drift:
            raise ValueError('Generated file drift: ' + ', '.join(drift))
    else:
        for path, data in expected.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(f'{"Checked" if args.check else "Built"}: {len(paths)} skill files, portable prompt, ZIP, SHA256SUMS')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, IndexError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
