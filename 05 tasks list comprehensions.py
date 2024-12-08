# [выражение for элемент in последовательность if условие]

# выражение — действие, которое применяется к каждому элементу.

# for элемент in последовательность — перебирает элементы.

# if условие (необязательно) — фильтрует элементы.

#Создание списка квадратов чисел:

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Вывод: [1, 4, 9, 16, 25]

#Фильтрация четных чисел:

numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Вывод: [2, 4, 6]

#Обработка строк:

names = ["Dias", "Rinat", "Dulat", "Igor", "Bakutzhan"]
short_names = [name for name in names if len(name) <= 5]
print(short_names)  # Вывод: ['Dias', 'Rinat', 'Igor']

'''Задание:
Создайте список чисел от 1 до 10.
С помощью спискового выражения создайте новый список, в который войдут только числа больше 5.
Создайте список квадратов всех четных чисел из этого диапазона.'''

numbers = [i for i in range(1, 11) if i >= 5]
print(numbers)  # Вывод: [5, 6, 7, 8, 9, 10]
numbers = [numbers[i]**2 for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(numbers)          # Вывод: [36, 64, 100]

'''
Chat GPT предложил упрощенный вариант решение задачи
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(squares_of_evens)  # Вывод: [36, 64, 100]'''

'''Вот упрощенные нами задачи в обычным коде, без листа компрехенсион

numbers2 = []
for i in range(1,11):
    if i >= 5:
        numbers2.append(i)
print(numbers2)

numbers3 = []
for i in numbers2:
    if i % 2 == 0:
        numbers3.append(i**2)
print(numbers3)'''