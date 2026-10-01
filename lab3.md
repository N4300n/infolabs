  # Lab 3. Toy Shell

Учебный проект: упрощённая командная оболочка («игрушечный шелл») на Python. Она принимает дату в формате `YYYY-MM-DD` и выводит файлы и папки текущей директории, которые были созданы раньше этой даты.

## Что такое toy shell

Toy shell — это упрощённая версия оболочки Unix/Linux (как Bash или Zsh). Её делают для обучения и экспериментов. Она повторяет только базовое поведение: принимает команды, разбирает их и выполняет. Скриптов, управления заданиями (job control) и сложной обработки ошибок здесь нет.

## Возможности

- Интерактивное приглашение `toy-shell>`
- Ввод даты в формате `YYYY-MM-DD`
- Вывод файлов и папок, созданных раньше указанной даты
- Для каждого элемента показывается тип (File / Folder) и время создания
- Проверка формата даты с понятным сообщением об ошибке
- Выход по команде `exit`; `Ctrl+C` не закрывает шелл

## Требования

- Linux / macOS (работает и на Windows, но установка в `/usr/local/bin` — только для Unix-систем)
- Python 3

Проверить, что Python установлен:

```bash
python3 --version
```
<img width="411" height="130" alt="image" src="https://github.com/user-attachments/assets/65554e71-3113-4612-b127-1c95208fb8db" />

---
## Код

Файл `toy_shell.py`:

```python
#!/usr/bin/env python3

import os
import time
from datetime import datetime

def list_items_older_than(date_input):
    try:
        # Parse the input date
        target_date = datetime.strptime(date_input, "%Y-%m-%d").timestamp()

        # Get the current directory items (files and folders)
        items = os.listdir('.')
        for item in items:
            # Get the creation time
            item_ctime = os.path.getctime(item)
            if item_ctime < target_date:
                # Determine if the item is a file or folder
                item_type = "Folder" if os.path.isdir(item) else "File"
                creation_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item_ctime))
                print(f"{item} ({item_type}, Created: {creation_time})")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def toy_shell():
    print("Toy Shell: List files and folders older than a given date (based on creation time)")
    print("Enter a date in the format YYYY-MM-DD or type 'exit' to quit.")
    while True:
        try:
            command = input("toy-shell> ").strip()
            if command.lower() == "exit":
                print("Exiting toy shell.")
                break
            list_items_older_than(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")

if __name__ == "__main__":
    toy_shell()
```
<img width="887" height="742" alt="image" src="https://github.com/user-attachments/assets/1ca3fe6b-b834-4c46-81dd-c5e6225478c6" />

---

## Запуск

Перейдите в папку с файлом и запустите:

```bash
python3 toy_shell.py
```
<img width="752" height="81" alt="image" src="https://github.com/user-attachments/assets/45f1bd07-1838-4811-9bb2-20f2bb8a84a5" />


Пример сессии:
```bash
toy-shell> 2027-01-10
.bashrc (File, Created: 2026-09-25 17:42:43)
.bash_history (File, Created: 2026-10-01 12:38:46)
toy_shell_test (Folder, Created: 2026-10-01 11:46:30)
.bash_logout (File, Created: 2026-09-25 17:42:43)
.landscape (Folder, Created: 2026-09-25 17:44:47)
.local (Folder, Created: 2026-09-25 17:47:16)
greet.sh (File, Created: 2026-09-25 17:50:00)
.cache (Folder, Created: 2026-09-25 17:44:47)
.config (Folder, Created: 2026-09-25 17:44:46)
test_words.txt (File, Created: 2026-10-01 11:29:54)
test_dir (Folder, Created: 2026-10-01 11:35:00)
.profile (File, Created: 2026-09-25 17:42:43)
.motd_shown (File, Created: 2026-10-01 11:03:53)
toy-shell>
```
<img width="760" height="440" alt="image" src="https://github.com/user-attachments/assets/f662da84-dbee-4afd-808c-a6a2ece07fe4" />

---

## Установка в систему (запуск из любой директории)

1. Переместите скрипт в папку, которая входит в `PATH`, например `/usr/local/bin`:

   ```bash
   sudo mv toy_shell.py /usr/local/bin/toy_shell
   ```
   
   <img width="663" height="41" alt="image" src="https://github.com/user-attachments/assets/a6c6b560-4ce5-4cd2-94b1-035a250a8e54" />


2. Сделайте файл исполняемым:

   ```bash
   sudo chmod +x /usr/local/bin/toy_shell
   ```

   <img width="587" height="24" alt="image" src="https://github.com/user-attachments/assets/00466f6f-c887-4b43-b17b-dd4707efd45a" />


3. Проверьте из любой директории:

   ```bash
   cd /some_directory
   toy_shell
   ```
   
   <img width="744" height="123" alt="image" src="https://github.com/user-attachments/assets/5efd3b05-a7ed-439a-90ee-eece8a746d20" />

> Это работает благодаря первой строке скрипта `#!/usr/bin/env python3` (shebang): система сама запускает файл через Python 3, а расширение `.py` для этого не нужно.
---

## Как это работает

### 1. Импорты

| Модуль | Зачем нужен |
|---|---|
| `os` | работа с файловой системой: список файлов, время создания, проверка на папку |
| `time` | преобразование времени из timestamp в читаемую строку |
| `datetime` | разбор введённой пользователем даты |

### 2. Функция `toy_shell()` — главный цикл

Это сама «оболочка». Она работает по классической схеме **REPL** (Read — Eval — Print — Loop):

1. **Read** — `input("toy-shell> ")` читает строку от пользователя, `.strip()` убирает лишние пробелы.
2. **Eval** — если введено `exit`, цикл прерывается. Иначе введённая строка считается датой и передаётся в `list_items_older_than`.
3. **Print** — функция выводит результат.
4. **Loop** — `while True` повторяет всё заново.

Блок `try / except KeyboardInterrupt` перехватывает `Ctrl+C`, поэтому шелл не падает с ошибкой, а подсказывает, что выйти нужно командой `exit`.

### 3. Функция `list_items_older_than(date_input)` — логика команды

1. **Разбор даты.** `datetime.strptime(date_input, "%Y-%m-%d")` превращает строку вида `2025-01-01` в объект даты, а `.timestamp()` — в число секунд с 1 января 1970 (Unix time). Так даты удобно сравнивать с временем файлов.
2. **Список элементов.** `os.listdir('.')` возвращает имена всех файлов и папок текущей директории (`.`).
3. **Время создания.** `os.path.getctime(item)` возвращает время элемента тоже в виде timestamp.
4. **Фильтр.** `if item_ctime < target_date` — оставляем только то, что создано раньше введённой даты.
5. **Тип элемента.** `os.path.isdir(item)` определяет, папка это или файл.
6. **Форматирование.** `time.localtime(...)` и `time.strftime(...)` превращают timestamp в строку `ГГГГ-ММ-ДД ЧЧ:ММ:СС`.
7. **Обработка ошибок.** Если формат даты неверный, `strptime` вызывает `ValueError`, и пользователь видит сообщение `Invalid date format`.

### 4. Точка входа

```python
if __name__ == "__main__":
    toy_shell()
```

Шелл запускается только при прямом запуске файла. При импорте как модуля он не стартует.
