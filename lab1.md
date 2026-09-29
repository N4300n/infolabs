# Lab 1 - Task 1: Управление директориями и файлами

**Цель:** Создать две директории, сгенерировать файлы в первой и переместить их во вторую с помощью PowerShell.

### Используемые команды
* `mkdir` — создание папки.
* `cd` — навигация.
* `New-Item` — создание файла.
* `mv` — перемещение файлов.
* `ls` — просмотр содержимого директории.

---


### Ход работы

**1. Создание директорий**
```powershell
mkdir dir1
mkdir dir2
```
<img width="778" height="478" alt="image" src="https://github.com/user-attachments/assets/726b71fb-4fb9-42e7-ba24-f4aa417c6293" />

**2. Создание файлов**
```powershell
cd .\dir1\
New-Item my_file.txt
New-Item my_file2.txt
```
<img width="1101" height="605" alt="image" src="https://github.com/user-attachments/assets/cc554faa-14ec-43a1-af05-1a6e5ae9c6a6" />

**3. Перемещение файлов в новую папку**
```powershell
cd ..
mv dir1\* dir2\
```
<img width="784" height="38" alt="image" src="https://github.com/user-attachments/assets/20f0fa79-6fa3-467c-90fa-5c61ace4ad1a" />

**Проверка результата**
```powershell
cd .\dir2\
ls
```
<img width="803" height="307" alt="image" src="https://github.com/user-attachments/assets/a58e611c-6d48-469f-9ea2-757c63bf817b" />
