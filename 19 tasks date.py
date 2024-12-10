'''from datetime import datetime

# Получение текущей даты и времени
now = datetime.now()
print("Текущая дата и время:", now)

# Отображение только даты
today = now.date()
print("Текущая дата:", today)

# Отображение только времени
current_time = now.time()
print("Текущее время:", current_time)'''


# Задача:
#
# Получает текущую дату и время.
# Выводит их в формате:
#
# Сегодня: 10.12.2024
# Текущее время: 09:30:15
#
# Вычисляет и выводит, какой день недели сегодня (например, "Сегодня вторник").
# Выводит дату и время, которые будут через 7 дней и 5 часов от текущего момента.
#
# Подсказки:
#
# Используйте методы модуля datetime:
# datetime.now() — текущие дата и время.
# strftime() — форматирование даты/времени.
# timedelta — добавление интервала времени.
# Для определения дня недели используйте .strftime('%A') (вернет название дня недели).
# Попробуйте решить, если нужна помощь — напишите! 😊

from datetime import datetime, timedelta

now = datetime.now()
today = now.date()
current_time = now.time()


print(f'Сегодня: {today}')
print(f'Текущее время: {now.strftime("%I:%M:%S")}')
print(f'Сегодня: {now.strftime("%A")}')

future_time = now + timedelta(days=7, hours=5)
print(f'Интервал времени через 5 часов и 7 дней: {future_time.strftime("%Y-%m-%d %I:%M:%S")}')