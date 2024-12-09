# Пример словаря
person = {
    "name": "Нурбек",
    "age": 29,
    "city": "Кокшетау"
}

# Доступ к значениям через ключи
print(person["name"])  # Вывод: Нурбек
print(person["age"])   # Вывод: 29

person["job"] = "Программист"  # Добавляем новую пару
person["age"] = 30  # Изменяем существующее значение
print(person)


person.pop("city")  # Удаляем по ключу
print(person)

for key, value in person.items():
    print(f"{key}: {value}")

if "name" in person:
    print("Ключ 'name' есть в словаре!")

print(person.keys())   # Список всех ключей
print(person.values()) # Список всех значений


# Создаём словарь для магазина
store = {
    "яблоки": 10,
    "бананы": 5,
    "апельсины": 8
}

# Выводим количество яблок
print(f"Яблоки в наличии: {store['яблоки']} кг")

# Добавляем товар
store["манго"] = 12

# Уменьшаем количество бананов
store["бананы"] -= 2

# Удаляем апельсины
store.pop("апельсины")

# Итоговый словарь
print(store)

# Задание:
# Создайте словарь с именами ваших друзей и их возрастами (например, "Dias": 29, "Rinat": 30).
# Выведите возраст каждого друга с помощью цикла.
# Добавьте нового друга в словарь.
# Удалите друга по имени.
# Проверьте, есть ли друг "Igor" в словаре.

friends = {
    'Dias': 29,
    'Rinat': 30,
    'Igor':20,
    'Bakutzhan':32,
}
for key,value in friends.items():
    print(f'Друг {key} ему {value} лет')

friends['Vladimir'] =30
print(friends)

friends.pop('Igor')

if "Igor" in friends:
    print("Ключ 'Igor' есть в словаре!")
else:
    print("Ключ 'Igor' нету в словаре!")