a, b = int(input("Введіть a: ")), int(input("Введіть b: "))

new_list = []

# 1
# for elem in range(a, b + 1):
#     if elem % 2 == 0:
#         new_list.append(elem)

# print(new_list)

# 2
print([elem for elem in range(a, b + 1) if elem % 2 == 0])