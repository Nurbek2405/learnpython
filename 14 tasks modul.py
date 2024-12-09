'''import math

# Использование функции из модуля math
result = math.sqrt(16)  # Выводит: 4.0
print(result)

# Импорт конкретной функции
from math import pi, sqrt

result = sqrt(25)  # Выводит: 5.0
print(result)

# Импорт всего содержимого модуля
from math import *

import simple_modul

result1 = simple_modul.add(5, 3)
result2 = simple_modul.subtract(10, 6)

print(result1)  # Выводит: 8
print(result2)  # Выводит: 4'''


# Задание:
# Создайте собственный модуль mymath.py с функциями:
#
# add(a, b) — возвращает сумму двух чисел.
# subtract(a, b) — возвращает разницу двух чисел.
# multiply(a, b) — возвращает произведение двух чисел.
# divide(a, b) — возвращает частное двух чисел (с проверкой на деление на ноль).
# В основной программе импортируйте этот модуль и вызовите все его функции, проверяя их работу.

import mymath

print(mymath.add(3,4))
print(mymath.subtract(3,4))
print(mymath.multiply(3,4))
print(mymath.divide(3, 1)) # Использует функцию из модуля mymath

