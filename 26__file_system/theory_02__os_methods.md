## Основные методы модуля `os`

| Метод                     | Назначение                                  | Пример                                      | Ожидаемый результат                                       |
|---------------------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------|
| `os.getcwd()`             | Возвращает текущую рабочую директорию       | `print(os.getcwd())`                        | Например: `C:\Users\User\project`                         |
| `os.chdir(path)`          | Меняет текущую рабочую директорию           | `os.chdir("folder")`                        | Текущая директория становится `folder`                    |
| `os.listdir(path)`        | Возвращает список файлов/папок в директории | `print(os.listdir("."))`                    | `['main.py', 'data', 'readme.txt']`                       |
| `os.mkdir(path)`          | Создаёт папку (1 уровень)                   | `os.mkdir("new_folder")`                    | Создаст каталог `new_folder`                              |
| `os.makedirs(path)`       | Создаёт вложенные папки                     | `os.makedirs("a/b/c")`                      | Создаст каталоги `a`, `a/b`, `a/b/c`                      |
| `os.rmdir(path)`          | Удаляет **пустую** папку                    | `os.rmdir("new_folder")`                    | Папка удаляется, если она пуста                           |
| `os.remove(path)`         | Удаляет файл                                | `os.remove("file.txt")`                     | Файл будет удалён                                         |
| `os.rename(src, dst)`     | Переименовывает файл или папку              | `os.rename("old.txt", "new.txt")`           | `old.txt` → `new.txt`                                     |
| `os.path.abspath(path)`   | Возвращает абсолютный путь                  | `print(os.path.abspath("data.txt"))`        | Например: `C:\Users\User\project\data.txt`                |
| `os.path.exists(path)`    | Проверяет существование пути                | `print(os.path.exists("data.txt"))`         | `True` или `False`                                        |
| `os.path.isdir(path)`     | Проверяет, является ли путь папкой          | `print(os.path.isdir("docs"))`              | `True` / `False`                                          |
| `os.path.isfile(path)`    | Проверяет, является ли путь файлом          | `print(os.path.isfile("main.py"))`          | `True` / `False`                                          |
| `os.path.join(a, b, ...)` | Правильно соединяет части пути              | `print(os.path.join("folder", "file.txt"))` | `folder/file.txt` (Linux) или `folder\file.txt` (Windows) |
| `os.sep`                  | Символ разделителя путей OS (зависит от ОС) | `print(os.sep)`                             | `/` (Linux/Mac) или `\` (Windows)                         |
| `os.path.split(path)`    | Разделяет путь на директорию и имя файла     | `os.path.split("folder/file.txt")`          | `('folder', 'file.txt')`               |
| `os.path.basename(path)` | Возвращает только имя файла или папки        | `os.path.basename("folder/file.txt")`       | `'file.txt'`                           |
| `os.path.dirname(path)`  | Возвращает только директорию без имени файла | `os.path.dirname("folder/file.txt")`        | `'folder'`                             |


## Отличие `os.mkdir` от `os.makedirs`

| Возможности                                        | Пример                                  | `os.mkdir` | `os.makedirs`             |
|----------------------------------------------------|-----------------------------------------| ---------- | ------------------------- |
| Может создать ТОЛЬКО одну вложенную папку          | `os.mkdir('folder1')`                   | ✅          | ❌                         |
| Может создавать вложенные папки                    | `os.makedirs('a/b/c')`                  | ❌          | ✅                         |
| Может не выбрасывать ошибку, если папка существует | `os.makedirs('folder2', exist_ok=True)` | ❌          | ✅ (`exist_ok=True`)       |
| Генерирует `FileExistsError`, если папка уже есть  | `os.mkdir('folder1')`                   | ✅          | ✅ (если `exist_ok=False`) |

