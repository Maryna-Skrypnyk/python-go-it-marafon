# Якщо параметр name не заданий, name = 'Alex'
def hello(name='Alex'):
    print('Hello, ', name, '!', sep='')


hello('Python')
hello()


def figure(type_figure, sw, color='black', x_cor=0, y_cor=0, f_size=12):
    print(type_figure, sw, color, x_cor, y_cor, f_size)


figure('квадрат', 20, 'green')
figure('квадрат', 36, 'red')
figure('квадрат', 28)
figure('квадрат', 12)
