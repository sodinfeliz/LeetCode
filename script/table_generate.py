from pathlib import Path



for path in Path('python/').glob('*.py'):
    print(path.stem)

