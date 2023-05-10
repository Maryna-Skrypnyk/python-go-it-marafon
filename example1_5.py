# input() — функція, яка зупиняє виконання програми,
# поки користувач не введе значення та натисне клавішу Enter.
# Функція повертає введене значення у типу даних рядок.

text = input("Enter some text: ")
print(text)
print(type(text))
print(len(text))

x = input("Enter some text: ")
x = int(x)
# x = x * 15
x *= 15
print(x)
print(int(input("Enter some text: ")) * 15)
