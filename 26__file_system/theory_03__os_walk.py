"""
os.walk - удобная рекурсивная функция, которая сама рекурсивно
обходит все директории, начиная от текущей
"""
import os

def print_tree(start_path="."):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, "").count(os.sep)
        indent = "│   " * level
        folder_name = os.path.basename(root) if os.path.basename(root) else root
        print(f"{indent}├── [{folder_name}]")

        # Сортируем, чтобы порядок был аккуратный
        files = sorted(files)
        dirs[:] = sorted(dirs)

        for i, file in enumerate(files):
            is_last = (i == len(files) - 1 and not dirs)  # последний только если нет подпапок ниже
            sub_indent = "│   " * (level + 1)
            branch = "└──" if is_last else "├──"
            print(f"{sub_indent}{branch} {file}")

print_tree(".")

#
# ├── [.]
# │   ├── homework_01.py
# │   ├── homework_02.py
# │   ├── homework_03.py
# │   ├── practice_work_01.py
# │   ├── practice_work_02.py
# │   ├── practice_work_03.py
# │   ├── theory_01__absolute_and_relative.md
# │   ├── theory_02__os_methods.md
# │   ├── theory_03__os_walk.py
# │   ├── theory_04__sys_argv.py
# │   ├── theory_05__.md
# │   ├── [solutions]
# │   │   ├── homework_01.py
# │   │   ├── homework_02.py
# │   │   └── homework_03.py