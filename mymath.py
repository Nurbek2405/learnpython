# add(a, b) — возвращает сумму двух чисел.

def add(a,b):
    return a+b

# subtract(a, b) — возвращает разницу двух чисел.

def subtract(a,b):
    return a-b

# multiply(a, b) — возвращает произведение двух чисел.

def multiply(a,b):
    return a*b

# divide(a, b) — возвращает частное двух чисел (с проверкой на деление на ноль).

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return print('Ошибка при деление на 0')
    finally:
        pass  # Не печатает "Программа завершена"

