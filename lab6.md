# Lab 6. Permissions in Linux
Права доступа в Linux определяют, кто может получать доступ к файлам и каталогам, изменять их или выполнять их. Грамотное управление правами доступа обеспечивает конфиденциальность и целостность данных, а также безопасность системы.

## Типы разрешений:
* Чтение (r): Просмотр содержимого файла или списка содержимого каталога.
* Запись (w): Изменение содержимого файла либо добавление или удаление файлов в каталоге.
* Выполнение (x): Запуск исполняемых файлов или получение доступа к содержимому каталога.

# Создание нового файла : 
```terminal
touch file.txt
````
<img width="373" height="55" alt="image" src="https://github.com/user-attachments/assets/7a2618b7-5b7b-4642-b98a-127138e97c85" />

# Права доступа к просмотру :

```terminal
ls -la file.txt
````

<img width="551" height="410" alt="image" src="https://github.com/user-attachments/assets/9593e067-85c0-4e1b-ac4f-f6955440ab31" />

# Измените права доступа, используя числовую нотацию :
```terminal
chmod 754 file.txt
````
<img width="560" height="483" alt="image" src="https://github.com/user-attachments/assets/cf4ac131-a2be-446f-8642-afbf8f58e851" />


<img width="577" height="429" alt="image" src="https://github.com/user-attachments/assets/d6668199-7010-4aa8-8413-3115d07a19aa" />


# Задание :
1. Создайте несколько файлов и каталогов с различными уровнями прав доступа.
2. Поэкспериментируйте с командами chmod, chown и chgrp для управления доступом.
3. Определите ситуации, в которых некорректно настроенные права доступа могут привести к уязвимостям в системе безопасности.
4. Подготовьте краткий обзор, посвященный важности аудита прав доступа и принципу минимальных привилегий.

### Задание 1: 


<img width="666" height="545" alt="image" src="https://github.com/user-attachments/assets/afd50cdc-17b5-4ee1-b8b5-601cfe775c63" />


<img width="664" height="616" alt="image" src="https://github.com/user-attachments/assets/12984e71-32bb-40d7-9e10-f146674c8b92" />

<img width="682" height="289" alt="image" src="https://github.com/user-attachments/assets/24af0284-8e0f-404d-83a3-eb07ca24d5c6" />

### Задание 2: 
