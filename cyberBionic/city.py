from turtle import *


def start_position(start_x, start_y):
    penup()
    goto(start_x, start_y)
    pendown()


def draw_back(start_x, start_y, colour, width_p, height_p):
    start_position(start_x, start_y)
    color(colour)
    begin_fill()
    for i in range(2):
        forward(width_p)
        left(90)
        forward(height_p)
        left(90)
    end_fill()


def draw_line(start_x, start_y, width_line):
    start_position(start_x, start_y)
    color('white')
    width(width_line)
    for i in range(25):
        forward(50)
        start_position(start_x + (75 * i), start_y)
    width(1)


def draw_road():
    draw_back(-400, -400, 'gray30', 800, 200)
    draw_line(-400, -258, 4)


def draw_cloud(start_x, start_y, my_color='white', radius=1):
    start_position(start_x, start_y)
    color(my_color)
    begin_fill()
    for _ in range(5):
        circle(radius)
        left(60)
    end_fill()


def draw_sun(start_x, start_y, size_line=30):
    start_position(start_x, start_y)
    begin_fill()
    color('orange', 'yellow')
    for i in range(18):
        forward(size_line)
        left(100)
    end_fill()


def draw_tree(start_x, start_y, color_trunk='honeydew4', color_tree='green4'):
    start_position(start_x, start_y)
    color(color_trunk)
    width(5)
    forward(10)
    left(180)
    forward(5)
    right(90)
    forward(100)
    left(90)
    forward(25)
    right(180)
    color(color_tree)
    width(15)
    for i in range(40):
        forward(50 - i)
        right(90)
        forward(10 * 3 + i)
        right(90)
    width(1)


def draw_square(length):
    begin_fill()
    for _ in range(4):
        forward(length)
        right(90)
    end_fill()


def draw_roof(start_x, start_y, col_r='brown4'):
    start_position(start_x, start_y)
    begin_fill()
    color(col_r)
    goto(start_x + 100, start_y + 50)
    goto(start_x + 200, start_y)
    goto(start_x, start_y)
    end_fill()


def draw_bg(start_x, start_y, col_bg='orange red'):
    start_position(start_x, start_y)
    color(col_bg)
    draw_square(200)


def draw_windows(start_x, start_y):
    start_position(start_x, start_y)
    color('white', 'light blue')
    for _ in range(3):
        draw_square(40)
        penup()
        forward(60)
        pendown()


def draw_building(start_x, start_y, col_bg='light salmon', col_roof='brown4', col_door='brown'):
    start_position(start_x, start_y)
    draw_bg(start_x, start_y, col_bg)
    draw_roof(start_x, start_y, col_roof)
    draw_windows(start_x + 20, start_y - 80)
    draw_windows(start_x + 20, start_y - 20)
    start_position(start_x + 70, start_y - 140)
    color(col_door)
    draw_square(60)


def draw_hospital(start_x, start_y, col_bg='wheat1', col_roof='gray4', col_door='black'):
    draw_building(start_x, start_y, col_bg, col_roof, col_door)
    start_position(start_x + 90, start_y + 25)
    width(5)
    color('red')
    forward(20)
    start_position(start_x + 100, start_y + 35)
    right(90)
    forward(20)


def main():
    draw_back(-400, 200, 'light cyan', 800, 200)
    draw_back(-400, 0, 'peach puff', 800, 200)
    draw_back(-400, -200, 'salmon1', 800, 200)
    draw_road()
    draw_cloud(-300, 300, 'SlateGray1', 25)
    draw_cloud(-250, 300, 'SlateGray2', 20)
    draw_cloud(-200, 300, 'SlateGray3', 25)
    draw_cloud(0, 300, 'SkyBlue1', 20)
    draw_cloud(50, 300, 'SkyBlue2', 15)
    draw_cloud(90, 300, 'SkyBlue3', 10)
    draw_sun(300, 280, 50)
    for i in range(7):
        draw_tree(-280 + 100 * i, 100 + 5 * i)
        draw_tree(-330 + 100 * i, 70 + 5 * i)
    draw_building(-350, 100)
    draw_building(150, 100)
    draw_hospital(-100, 50)


if __name__ == '__main__':
    speed(0)
    main()

    hideturtle()
    exitonclick()
