name = None  # спочатку ми не знаємо імені користувача

# нескінченний цикл
while True:
    print("Меню:\n1. Ввести ім'я\n2. Вивести вітання\n3. Вийти")

    response = input('Оберіть пункт: ')
    print()

    if response == '1':
        name = input("Введіть ваше ім'я: ")
    elif response == '2':
        if name:  # вітаємося з користувачем, якщо ім'я вже введене
            print('Привіт, ', name, '!', sep='')
        else:
            print('Я не знаю вашого імені.')
    elif response == '3':
        # оператор break завершує виконання циклу
        break  # якщо користувач вибрав третій пункт, то виходимо із циклу
    else:
        print('Неправильне введення.')

    print()