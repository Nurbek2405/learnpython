# Генератор для создания последовательности квадратов чисел
'''def square_numbers(limit):
    for i in range(limit):
        yield i ** 2

squares = square_numbers(5)
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9
print(next(squares))  # 16'''

# Создайте генератор even_numbers(limit), который возвращает все чётные числа от 0 до limit (включительно).
# Используйте его, чтобы вывести все чётные числа до 10.

'''def even_numbers(limit):
    for i in range(0,limit+1,2):
        yield i

evens = even_numbers(10)
for i in evens:
    print(i)'''

# print(next(evens))  # 0
# print(next(evens))  # 2
# print(next(evens))  # 4
# print(next(evens))  # 6
# print(next(evens))  # 8
# print(next(evens))  # 10

'''Создайте генератор, который принимает число n и 
генерирует квадраты чисел от 1 до n. 
Выведите все квадраты, используя цикл for.'''

'''def squares_n (limit):
    for i in range(1,limit+1):
        yield i ** 2

square = squares_n(5)
for i in square:
    print(i)
'''

def odd_numbers(limit):
    for i in range (1,limit,2):
        yield i

odds = odd_numbers(10)
for num in odds:
    print(num)