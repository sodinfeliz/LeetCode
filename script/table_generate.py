import re
from pathlib import Path

def extract(path: Path):
    num, title = str(path.stem).split(sep='_', maxsplit=1)
    title = title.replace('_', ' ')
    lines = open(str(path), 'r').read().splitlines()[1:5]
    qlink = re.findall('^Question Link: (.*)', lines[0])[0]
    diff = re.findall('^Difficulty: (.*)', lines[1])[0]

    return num, title, qlink, diff


def main():
    src_paths = list(Path('python/').glob('*.py'))[::-1]
    with open('./script/README_table.md', 'w') as f:
        f.write('| # | Title | Solution | Difficulty |\n')
        f.write('|---| ----- | -------- | ---------- |\n')
        
        for path in src_paths:
            num, title, qlink, diff = extract(path)
            f.write(f'| {num} | [{title}]({qlink}) | [Python](./python/{path.name}) | {diff} |\n')

main()

