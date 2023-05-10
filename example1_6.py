# Числа у десятковій системі числення
decimal_1 = 28
decimal_2 = -3

print(decimal_1)
print(decimal_2)
# порожній print для перенесення рядка
print()

# Числа у шістнадцятковій системі числення
hexadecimal_1 = 0x9
hexadecimal_2 = 0xA

print(hexadecimal_1)
print(hexadecimal_2)
print()

# Число в двійковій системі числення
bin1 = 0b11101101
print(bin1)
print()

# Число у вісімковій системі числення
oct1 = 0o765
print(oct1)
print()

# Побудова цілого числа з іншого значення
string = "15"
number = string
print(number)
print(string)
print(number + str(5))
# string + 5 -- помилка TypeError: can only concatenate str (not "int") to str
print(int(number) + 5)
print(number * 5)
print(int(number) * 5)
