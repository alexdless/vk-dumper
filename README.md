# vk-dumper
Public unloading subscribers in sqlite\выгрузка подписчиков паблика в sqlite

Алгоритм работы:

----аутентификация vk api----
Ваш логин и пасс от вк

----ввод id паблика----
...

----работа с vk api----
Использование метода groups.getMembers для выгрузки списка пользователей паблика

----DB----
Создание базы sqlite, запись всех данных в таблицу "users"
Поля: 
>id INT
>first_name TEXT
>last_name TEXT
>city TEXT
