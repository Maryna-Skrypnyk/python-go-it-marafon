MY_NAME = "Maryna"
answer = input("Enter your name: ")

# 1 Звичайна умова
if answer == MY_NAME:
    print("Your name is the same as mine")
else:
    print("We have different names")

# 2 Через тернарний оператор
print("Your name is the same as mine" if answer == MY_NAME else "We have different names")