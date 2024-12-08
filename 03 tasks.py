while True:  # Бесконечный цикл
    user_input = input("Введите число (или нажмите Enter для выхода): ")

    if user_input == '':  # Проверка на пустую строку
        break  # Прерывание цикла

    print(f"Вы ввели: {user_input}")


