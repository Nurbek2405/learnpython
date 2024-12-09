'''# Создайте текстовый файл 'example.txt' с текстом "Привет, Нурбек!"
file = open('files/example.txt', 'r', encoding='utf-8')  # Открываем файл для чтения
content = file.read()           # Читаем содержимое файла
print(content)                  # Выводим текст файла
file.close()                    # Закрываем файл

file = open('files/example.txt', 'w', encoding='utf-8')  # Открываем файл для записи
file.write("Новая запись в файле!")  # Записываем строку
file.close()

file = open('files/example.txt', 'a', encoding='utf-8')  # Открываем файл для добавления
file.write("\nДобавляем ещё одну строку!")  # Добавляем строку
file.close()

with open('files/example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)'''

# Задание:
# Создайте файл my_friends.txt и запишите туда список друзей (каждое имя с новой строки).
# Откройте этот файл для чтения и выведите содержимое на экран.
# Допишите в файл фразу "Все друзья лучшие!".
# Проверьте, как изменилось содержимое файла.

def reading():
    with open('files/my_friends.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

reading()

file = open('files/my_friends.txt', 'a', encoding='utf-8')  # Открываем файл для добавления
file.write("\nВсе друзья лучшие!")  # Добавляем строку
file.close()

print('\nПосле добавление новой строки в файл')
reading()


'''Идеи для улучшения:
Если вы хотите сделать ваш код ещё более универсальным, можно передавать имя файла в функцию как параметр:

python
Копировать код
def reading(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

# Чтение конкретного файла
reading('files/my_friends.txt')'''