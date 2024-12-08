# number = int(input("Введите число: "))  # Если пользователь введёт "abc", будет ошибка ValueError.

# try:
#     # Код, где может возникнуть ошибка
# except ТипИсключения:
#     # Код для обработки ошибки

'''try:
    a = int(input("Введите число: "))
    b = int(input("Введите делитель: "))
    result = a / b
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")
except ValueError:
    print("Ошибка: Нужно вводить только числа.")'''

'''try:
    a = int(input("Введите число: "))
    b = int(input("Введите делитель: "))
    result = a / b
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена.")'''

# Задание:
# Запрашивает у пользователя два числа.
# Делит первое число на второе.
# Обрабатывает ошибки ZeroDivisionError и ValueError.
# В блоке finally выведите сообщение "Программа завершила обработку."

try:
    a = int(input("Введите число: "))
    b = int(input("Введите делитель: "))
    result = a / b
except ValueError:
    print("Ошибка: Нужно вводить только числа!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершила обработку.")

#Ваш прогресс: Поздравляю, вы освоили обработку исключений! Теперь ваш прогресс составляет 45%