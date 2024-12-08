text = "   Hello, World!   "

# Преобразование к верхнему и нижнему регистру
print(text.upper())  # "   HELLO, WORLD!   "
print(text.lower())  # "   hello, world!   "

# Удаление пробелов
print(text.strip())  # "Hello, World!"

# Замена подстроки
new_text = text.replace("World", "Python")
print(new_text)  # "   Hello, Python!   "

# Разделение строки на список слов
words = text.split(", ")
print(words)  # ['   Hello', 'World!   ']

# Объединение списка в строку
joined_text = ", ".join(words)
print(joined_text)  # "   Hello, World!   "

# Поиск подстроки
index = text.find("World")
print(index)  # 9

# Подсчёт вхождений
count = text.count("l")
print(count)  # 3

# Задание:

# Запрашивает у пользователя строку текста.
# Преобразует текст в верхний регистр.
# Удаляет начальные и конечные пробелы.
# Заменяет все буквы "а" на "e".
# Разделяет строку на отдельные слова.
# Объединяет слова обратно в строку через запятую.
# Выводит длину строки.
print('###################################################')

text_simple = 'Hello my friends and people in Kokshetay!'
text_simple2 = text_simple.upper()
text_simple6 = text_simple.strip()
text_simple3 = text_simple2.replace('A','E')
text_simple4 = text_simple3.split(' ')
text_simple5 = ', '.join(text_simple4)
print(text_simple5)
print(len(text_simple5))

# Ваш прогресс:
# Вы успешно освоили основные методы работы со строками в Python! Теперь ваш прогресс составляет 50%. 🎉
