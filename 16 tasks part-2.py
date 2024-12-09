'''class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Это животное издает звук."

class Dog(Animal):  # Класс Dog наследует Animal
    def speak(self):
        return f"{self.name} лает."

class Cat(Animal):  # Класс Cat наследует Animal
    def speak(self):
        return f"{self.name} мяукает."

# Создаем объекты
dog = Dog("Барсик")
cat = Cat("Мурка")

print(dog.speak())  # Ожидаемый вывод: Барсик лает.
print(cat.speak())  # Ожидаемый вывод: Мурка мяукает.'''
import math

# Задача для вас:
# Создайте классы Transport (родительский класс) и два дочерних класса: Car и Bicycle.
# Реализуйте следующее:
#
# В классе Transport добавьте атрибут name (название транспорта) и метод move(),
# который возвращает строку "Этот транспорт передвигается."
# В классе Car переопределите метод move, чтобы он возвращал "Машина едет на дороге."
# В классе Bicycle переопределите метод move, чтобы он возвращал "Велосипед едет по велодорожке."

'''class Transport:
    def __init__(self, name):
        self.name = name

    def move(self):
        return 'Этот транспорт передвигается.'

class Car(Transport):
    def move(self):
        return f'{self.name} едет на дороге.'

class Bicycle(Transport):
    def move(self):
        return f'{self.name} едет по велодорожке.'

car = Car('Toyota Camri')
bicycle = Bicycle('Mointaun Bicycle')

print(car.move())
print(bicycle.move())
'''

# Прекрасно! 🚀 Давайте разберем следующую задачу.
# Задание:
# Создайте иерархию классов для работы с фигурами. У вас будет базовый класс Shape, от которого
# будут наследоваться классы Triangle и Square.

# Условия:
# Класс Shape:  Имеет метод get_area, который возвращает "Неопределённая площадь"(для
# базового класса). Метод get_perimeter, возвращающий "Неопределённый периметр".

# Класс Triangle:

# Инициализируется тремя сторонами: a, b, c. Реализует метод get_perimeter, возвращающий
# сумму всех сторон. Реализует метод get_area по формуле
# Герона: 𝑠 = 𝑎 + 𝑏 + 𝑐 2 ,
# Площадь = 𝑠 ⋅ (𝑠 − 𝑎 ) ⋅ ( 𝑠 − 𝑏 ) ⋅ ( 𝑠 − 𝑐 )
# s = 2 a + b + c ​ , Площадь = s⋅(s−a)⋅(s−b)⋅(s−c) ​

# Класс Square:
# Инициализируется длиной стороны side. Реализует метод get_perimeter, возвращающий
# периметр квадрата. Реализует метод get_area, возвращающий площадь квадрата.

class Shape:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return "Неопределённая площадь"

    def get_perimeter(self):
        return "Неопределённый периметр"

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a,b,c)

    def get_perimeter(self):
        return self.a+self.b+self.c

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return 4 * self.side

    def get_area(self):
        return self.side ** 2

triangle = Triangle(3, 4, 5)
print(triangle.get_perimeter())  # Ожидаемый вывод: 12
print(round(triangle.get_area(), 2))  # Ожидаемый вывод: 6.0

square = Square(4)
print(square.get_perimeter())  # Ожидаемый вывод: 16
print(square.get_area())  # Ожидаемый вывод: 16
