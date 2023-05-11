# Створюємо список
my_list = ["One", "piece", "per", "time"]

# Отримуємо ітератор за допомогою iter()
my_iter = iter(my_list)
print(type(my_iter))
# Ітеруємо об'єкт за допомогою next()

# Відображення: One
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Відображення: piece
print(next(my_iter))

# Відображення: per
print(next(my_iter))

# Відображення: time
print(next(my_iter))

# Наступний виклик викине виняток StopIteration, оскільки елементи закінчилися
next(my_iter)
