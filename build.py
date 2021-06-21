import os

cmds = [
    "python -m black .",
    "python -m pylint scrapetools",
    "mypy --ignore-missing-imports --strict scrapetools",
    "python -m pytest tests",
]

for cmd in cmds:
    print(f"Executing command {cmd}")
    os.system(cmd)
