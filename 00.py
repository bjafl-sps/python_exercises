from pathlib import Path
import re
folder_path = Path('./solutions')

def fix_print(f):
    with open(f, 'r') as file:
        lines = file.readlines()
    for line in lines:
        m = re.match('print\(.+$', line)
        if m:
            m = m.group().strip() + ')'
            line = m
    with open(f, 'w') as file:
        file.writelines(lines)
        


# Get all files using list comprehension
for file in folder_path.iterdir():
    if file.name.endswith('.py'):
        fix_print(file)