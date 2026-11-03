"""Read-only packaging/public-data checks; not full YAML or behavior validation."""
from pathlib import Path
import json
import re
import sys

LOCAL_PATH = re.compile(
    r'\b[A-Za-z]:[\\/]|\\\\(?:[A-Za-z0-9]|[?.]\\)|file:/|'
    r'(?<![\w.])/(?:home|Users|root|mnt|private|tmp|var|etc)(?:/|$)',
    re.I,
)


def check(root):
    root = root.resolve()
    failures = []
    skill = root / 'skills/context-workflow/SKILL.md'
    if not skill.is_file():
        return ['missing SKILL.md'], 0
    if not skill.resolve().is_relative_to(root):
        return ['SKILL.md source escapes package; not read'], 0
    content = skill.read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
    if not front:
        failures.append('frontmatter boundaries missing')
    else:
        fields = front.group(1)
        if not re.search(r'^name: context-workflow$', fields, re.M):
            failures.append('name/directory mismatch')
        description = re.search(r'^description: "([^\n]+)"$', fields, re.M)
        if not description or not 1 <= len(description.group(1)) <= 1024:
            failures.append('description missing/invalid in supported subset')
    if len(content.splitlines()) > 80:
        failures.append('entrypoint exceeds preview budget')
    links = 0
    for path in sorted(root.rglob('*')):
        if '.git' in path.parts or not path.is_file() or path.suffix not in {'.md', '.yaml', '.json'}:
            continue
        label = path.relative_to(root).as_posix()
        if not path.resolve().is_relative_to(root):
            failures.append(f'{label}: escaping source path; not read')
            continue
        text = path.read_text(encoding='utf-8')
        if LOCAL_PATH.search(text):
            failures.append(f'{label}: machine-local absolute path')
        if re.search(r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----', text):
            failures.append(f'{label}: private-key marker')
        if any(line != line.rstrip() for line in text.splitlines()):
            failures.append(f'{label}: trailing whitespace')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('http:', 'https:', '#')):
                continue
            resolved = (path.parent / target.split('#')[0]).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                failures.append(f'{label}: missing/escaping relative link')
            links += 1
    cases = json.loads((root / 'evals/cases.json').read_text(encoding='utf-8'))['cases']
    if len({case['id'] for case in cases}) != len(cases):
        failures.append('duplicate case identity')
    return failures, links


if __name__ == '__main__':
    project = Path(__file__).resolve().parents[1]
    problems, count = check(project)
    print(json.dumps({'relative_links_checked': count, 'failures': problems,
                      'scope': 'packaging/subset metadata/public markers only; not behavior or full secret audit'}))
    sys.exit(bool(problems))
