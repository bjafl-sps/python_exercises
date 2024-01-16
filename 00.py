from pathlib import Path
import re
folder_path = Path('./solutions')

def fix_print(f:Path):
    with open(f, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        m = re.match('^( +)?print', lines[i])
        if m:
            new_l = re.sub('( +)?\n', ')\n', lines[i])
            new_l = re.sub('(?<=print) ', '(', new_l)
            lines[i] = new_l
    new_path = f.parent.joinpath('fix', f.name)
    with open(new_path, 'w') as file:
        file.writelines(lines)
        


# Get all files using list comprehension
for file in folder_path.iterdir():
    if file.name.endswith('.py'):
        fix_print(file)