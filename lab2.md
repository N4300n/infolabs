# Lab 2: Custom UNIX-based commands

Пользовательские команды в терминале Unix — это созданные пользователем скрипты, которые выполняют определенные задачи. Они повышают производительность за счет автоматизации повторяющихся действий или объединения нескольких команд в одну.

В этом репозитории представлены учебные проекты по созданию системных скриптов. Все скрипты размещаются в директории `/usr/local/bin/`, что позволяет вызывать их как стандартные команды терминала.

## Общий алгоритм создания команды

Для каждого скрипта необходимо выполнить следующие шаги:

1. Создать файл: `sudo nano /usr/local/bin/<имя_скрипта>`
2. Вставить код скрипта (представлен ниже для каждого задания).
3. Сделать файл исполняемым: `sudo chmod +x /usr/local/bin/<имя_скрипта>`
4. Протестировать, введя в терминал: `<имя_скрипта>`

---

## Пример: Вывод системной информации (`system_info`)

**Описание:**
Скрипт выводит имя хоста, имя текущего пользователя и информацию о свободном дисковом пространстве.

**Использование:**

```bash
system_info
```

<img width="812" height="486" alt="image" src="https://github.com/user-attachments/assets/961486b2-038d-4581-8d08-e4e6508adb1e" />

**Код скрипта:**

```bash
#!/bin/bash

echo "Hostname: $(hostname)"
echo "Current User: $(whoami)"
echo "Disk Space: $(df -h)"
```

<img width="574" height="36" alt="image" src="https://github.com/user-attachments/assets/b1901b6c-477a-4fac-9459-c192e49cb6aa" />

<img width="1112" height="633" alt="image" src="https://github.com/user-attachments/assets/29171962-cf61-495a-9bd8-be536913e7c7" />

---

## 1. Скрипт приветствия (`greet.sh`)

**Описание:**
Скрипт выводит приветственное сообщение с именем текущего пользователя системы.

**Использование:**

```bash
greet.sh
```

<img width="807" height="461" alt="image" src="https://github.com/user-attachments/assets/d6511de5-21f9-4f89-9155-563cda84c8d7" />

**Код скрипта:**

```bash
#!/bin/bash

echo "Hello, $(whoami)!"
```

---

## 2. Скрипт времени до конца рабочего дня (`current_time.sh`)

**Описание:**
Скрипт отображает текущее время и рассчитывает, сколько часов и минут осталось до конца рабочего дня (до 18:00).

**Использование:**

```bash
current_time.sh
```

**Код скрипта:**

```bash
#!/bin/bash

current_time=$(date +"%H:%M")
current_hour=$(date +"%H")
current_min=$(date +"%M")

current_total_mins=$((10#$current_hour * 60 + 10#$current_min))
end_total_mins=$((18 * 60))

if [ "$current_total_mins" -lt "$end_total_mins" ]; then
    diff_mins=$((end_total_mins - current_total_mins))
    hours_left=$((diff_mins / 60))
    mins_left=$((diff_mins % 60))
    echo "Current time: $current_time. Work day ends after $hours_left hours and $mins_left minutes."
else
    echo "Current time: $current_time. The work day has already ended!"
fi
```

---

## 3. Скрипт подсчета совпадений слова в файле (`count_word.sh`)

**Описание:**
Скрипт принимает два аргумента (имя файла и слово) и подсчитывает, сколько раз указанное слово встречается в этом файле.

**Использование:**

```bash
count_word.sh <имя_файла> <слово>
```

**Код скрипта:**

```bash
#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: count_word.sh <file_name> <word>"
    exit 1
fi

file=$1
word=$2

if [ ! -f "$file" ]; then
    echo "Error: File '$file' not found."
    exit 1
fi

count=$(grep -o -i "$word" "$file" | wc -l)

echo "The word '$word' appears $count times in '$file'."
```

---

## 4. Скрипт для поиска и удаления пустых файлов (`delete_empty_files.sh`)

**Описание:**
Скрипт принимает путь к директории в качестве аргумента, находит в ней все пустые файлы, удаляет их и выводит имена удаленных файлов на экран.

**Использование:**

```bash
delete_empty_files.sh <путь_к_директории>
```

**Код скрипта:**

```bash
#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: delete_empty_files.sh <directory>"
    exit 1
fi

DIR=$1

if [ ! -d "$DIR" ]; then
    echo "Error: Directory '$DIR' does not exist."
    exit 1
fi

empty_files=$(find "$DIR" -type f -empty)

if [ -z "$empty_files" ]; then
    echo "No empty files found in '$DIR'."
else
    echo "Deleted the following empty files:"
    for file in $empty_files; do
        echo "$file"
        rm "$file"
    done
fi
```







<img width="537" height="25" alt="image" src="https://github.com/user-attachments/assets/68ca309b-a459-4fbb-b7c1-99f226eb2477" />

<img width="1119" height="623" alt="image" src="https://github.com/user-attachments/assets/c260f622-98c2-45c1-ae0d-f85ad4006759" />
<img width="595" height="76" alt="image" src="https://github.com/user-attachments/assets/6ab5a8b7-3e75-4175-81da-45714fe3f177" />
<img width="1003" height="442" alt="image" src="https://github.com/user-attachments/assets/560bbc6d-fc53-476a-b70a-0fa0c23652ec" />
<img width="674" height="75" alt="image" src="https://github.com/user-attachments/assets/9492ef1a-f5b9-4018-b38f-77dd04ba4fc7" />
<img width="633" height="185" alt="image" src="https://github.com/user-attachments/assets/3b51eae9-7275-4bfb-96ac-c2e1412960b4" />
<img width="555" height="658" alt="image" src="https://github.com/user-attachments/assets/87810f42-e4a9-4cf5-bc13-a18d160c5938" />
