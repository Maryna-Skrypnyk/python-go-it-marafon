import turtle

# Шестикутник
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)

turtle.color('green')
turtle.width(4)
for i in range(6):
    turtle.forward(100)
    turtle.left(60)

turtle.exitonclick()


# Квадрат
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.color('green')
turtle.width(4)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()