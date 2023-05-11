x = 10

for row in range(x):
    for col in range(x):
        if col <= row:
            print('*', end=' ')
        else:
            print("", end='')
    print()
