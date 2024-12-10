# Простая задача: Создание базы данных
# Задача: Создайте базу данных library.db и таблицу books, где будут храниться данные о книгах:
#
# id (целое число, автоинкремент),
# title (строка),
# author (строка),
# year (целое число).

import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('library.db')

# Создание таблицы
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
)
''')

# Закрытие соединения
connection.close()

# Теперь мы можем перейти к следующим шагам, связанным с работой с базой данных:
#
# Вставка данных: добавление информации о книгах.
# Выборка данных: чтение информации из таблицы.
# Обновление и удаление записей.

# Задача: Вставка данных
# Добавьте в таблицу books три книги с информацией о названии,
# авторе и годе издания.

# Подключение к базе данных
connection = sqlite3.connect('library.db')
cursor = connection.cursor()

# Вставка данных
cursor.execute("INSERT INTO books (title, author, year) VALUES ('1984', 'George Orwell', 1949)")
cursor.execute("INSERT INTO books (title, author, year) VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960)")
cursor.execute("INSERT INTO books (title, author, year) VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1925)")

# Сохранение изменений
connection.commit()


# Закрытие соединения
connection.close()
