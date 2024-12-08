'''Параметры и аргументы
Параметры задаются при создании функции.
Аргументы передаются при вызове

def greet(name):
    return f"Привет, {name}!"

# Вызов функции
print(greet("Нурбек"))  # Вывод: Привет, Нурбек!'''

'''Функция без параметров: Иногда параметры не нужны:

def add(a, b):
    return a + b

print(add(3, 5))  # Вывод: 8'''

'''
Функция с несколькими параметрами и значениями по умолчанию:

ef power(base, exponent=2):  # По умолчанию степень = 2
    return base ** exponent

print(power(3))       # 9 (3^2)
print(power(2, 3))    # 8 (2^3)
'''

''' Задание 1) Напишите функцию multiply(a, b), которая возвращает произведение двух чисел.'''
'''Задание 2 Напишите функцию is_even(number), которая возвращает True, 
если число чётное, и False, если нечётное.'''

def multiply(a, b):
    return print(a * b)

def is_even (number):
    if number % 2 == 0:
        return print(True)
    else:
        return print(False)

multiply(3, 5)
is_even(5)


'''def multiply(a, b):
    return a * b

def is_even(number):
    return number % 2 == 0

print(f"Произведение: {multiply(3, 5)}")  # Вывод: Произведение: 15
print(f"Число 5 чётное? {is_even(5)}")  # Вывод: Число 5 чётное? False'''



