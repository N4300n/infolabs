# Lab 5. User Management in Linux
Управление пользователями в Linux включает создание, изменение и администрирование учетных записей пользователей и групп в системе. Это обеспечивает безопасный доступ, а также установку надлежащих прав доступа к файлам, каталогам и процессам.
## К числу основных задач относятся:

* Создание пользователей: добавление новых пользователей с помощью таких команд, как `adduser` или `useradd`.
* Изменение параметров пользователей: корректировка свойств учетной записи (например, домашнего каталога, командной оболочки, пароля) с помощью команд `usermod` или `passwd`.
* Удаление пользователей: ликвидация учетных записей с помощью команды `userdel`.
* Управление группами: работа с группами посредством команд `groupadd`, `groupmod` и `groupdel`.
* Управление правами доступа: включение пользователей в группы, а также настройка прав доступа к файлам и каталогам (с использованием команд `chmod`, `chown`, `chgrp`).
* Мониторинг пользователей: отслеживание пользователей, работающих в системе в данный момент, с помощью команд `who` или `w`.
* Информация о пользователях и группах хранится в таких конфигурационных файлах, как `/etc/passwd`, `/etc/shadow` и `/etc/group`.
# Creating new user. 
```terminal
sudo adduser user1
```
<img width="550" height="447" alt="image" src="https://github.com/user-attachments/assets/66c1c654-e37c-408b-b553-a19104366eb4" />

# Verify the user creation by running:
```terminal
cat /etc/passwd
```
<img width="662" height="575" alt="image" src="https://github.com/user-attachments/assets/b1b1e1ef-49cb-46d0-9135-ea35539c0f01">

# Login as new user:

<img width="752" height="440" alt="image" src="https://github.com/user-attachments/assets/f34c4740-9f70-46a4-9039-7ee6fbd1ca47" />

---
```terminal
whoami
```
<img width="607" height="111" alt="image" src="https://github.com/user-attachments/assets/95aa28b9-84fb-485c-851a-d799eacf9a22" />

# Change personal information
```terminal
chfn
```
<img width="482" height="177" alt="image" src="https://github.com/user-attachments/assets/21b207fa-e3c9-4a2d-bcf2-f01f92d413bc" />

--- 
<img width="662" height="620" alt="image" src="https://github.com/user-attachments/assets/4183ce02-4497-4fbd-bd47-1dd7fcc04299" />

# Delete the user
```terminal
pkill -KILL -u user1
````
<img width="426" height="35" alt="image" src="https://github.com/user-attachments/assets/e47e5a17-acbb-46b3-b8ec-23aceec2a2ff" />

```terminal
sudo deluser --remove-home user1
````
<img width="666" height="616" alt="image" src="https://github.com/user-attachments/assets/d93fb126-2856-47ec-9d24-b7ec7aa3aa63" />

