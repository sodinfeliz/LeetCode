from pathlib import Path

def extract(path: Path):
    num, title = str(path.stem).split(sep='_', maxsplit=1)
    title = title.replace('_', ' ')



def main():
    src_paths = list(Path('python/').glob('*.py'))[::-1]
    with open('README_table.md', 'w') as f:
        f.write('| # | Title | Solution | Difficulty |\n')
        f.write('|---| ----- | -------- | ---------- |\n')





