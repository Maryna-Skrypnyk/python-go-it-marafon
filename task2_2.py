# 1 Коли числа задані
a = 1
b = 20

while a <= b:
    print(a)
    a += 1

# 2 Коли числа задає користувач
while True:
    print()
    a, b = int(input("Введіть a: ")), int(input("Введіть b: "))

    if a <= b:
        while a <= b:
            print(a)
            a += 1
        break
    else:
        print()
        print('"b" повинно бути більшим, ніж "a". Спробуйте ще раз.')

# 3 Range при заданих числах
a = 1
b = 20

for i in range(a, b + 1):
    print(i)
        
# 4 Range, коли числа задає користувач
while True:
    print()
    a, b = int(input("Введіть a: ")), int(input("Введіть b: "))

    if a <= b:
        while a <= b:
            for i in range(a, b + 1, 1):
                print(i)
            break
        break
    else:
        print()
        print('"b" повинно бути більшим, ніж "a". Спробуйте ще раз.')        