#Определение класса и создание объекта:

'''class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} {self.year}")'''

#Наследование:

'''my_car = Car("Toyota", "Camry", 2021)
my_car.display_info()  # Вызов метода display_info на объекте my_car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  # Вызов конструктора родительского класса
        self.battery_size = battery_size

    def display_info(self):
        super().display_info()
        print(f"Battery size: {self.battery_size} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
my_electric_car.display_info()'''

# Инкапсуляция:

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Приватный атрибут

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Возраст должен быть положительным")

person = Person("Alice", 30)
print(person.get_age())
person.set_age(35)
print(person.get_age())
'''

#Полиморфизм:

'''class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Вывод: Woof!
animal_sound(cat)  # Вывод: Meow!'''

# Задача: Создание класса "Круг"
# Условие:
# Создайте класс Circle, который будет представлять круг. Класс должен иметь следующие свойства и методы:
#
# Атрибут radius (радиус круга).
# Метод get_area, который возвращает площадь круга.
# Формула площади: 𝜋×𝑟2 π×r2 , где 𝑟 r — радиус.
# Метод get_circumference, который возвращает длину окружности.
# Формула длины окружности: 2𝜋×𝑟 2π×r.
# Пример работы программы:
#
# circle = Circle(5)  # Создаем круг с радиусом 5
# print(circle.get_area())  # Ожидаемый вывод: 78.54 (приблизительно)
# print(circle.get_circumference())  # Ожидаемый вывод: 31.42 (приблизительно)
# Подсказка:
#
# Используйте модуль math для получения значения числа 𝜋 π.

'''import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return self.radius ** 2 * math.pi
    
    def get_circumference(self):
        return 2 * math.pi * self.radius
    
circle = Circle(5)  # Создаем круг с радиусом 5
print(circle.get_area())  # Ожидаемый вывод: 78.54 (приблизительно)
print(circle.get_circumference())  # Ожидаемый вывод: 31.42 (приблизительно)'''

# Задача 1: Класс "Прямоугольник"
# Условие:
# Создайте класс Rectangle, который будет представлять прямоугольник. Класс должен иметь следующие свойства и методы:
#
# Атрибуты length (длина) и width (ширина).
# Метод get_area, который возвращает площадь прямоугольника.
# Формула площади: длина × ширина
#
# Метод get_perimeter, который возвращает периметр прямоугольника.
# Формула периметра: 2×(длина+ширина)

'''class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def get_area(self):
        return self.length * self.height

    def get_perimeter(self):
        return 2 * (self.length + self.height)

rectangle = Rectangle(10, 5)  # Создаем прямоугольник с длиной 10 и шириной 5
print(rectangle.get_area())  # Ожидаемый вывод: 50
print(rectangle.get_perimeter())  # Ожидаемый вывод: 30'''

'''Задача 2: Класс "Книга"
Условие:
Создайте класс Book, который будет представлять книгу. Класс должен иметь следующие свойства и методы:

Атрибуты:
title (название),
author (автор),
year (год издания).
Метод get_description, который возвращает строку в формате:
"Название книги: [title], Автор: [author], Год издания: [year]".'''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

book = Book('Harry Potter','Dzh. K. Rouling',1992)

print(book.get_description())