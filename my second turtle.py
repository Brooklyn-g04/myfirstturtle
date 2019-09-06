import turtle
size = 0



turtle.speed(100)
turtle.color("violet")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)

    size += 3

turtle.penup()
turtle.goto(100, -100)
turtle.pendown()


def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)

    size += 3

turtle.penup()
turtle.goto(200, 100)
turtle.pendown()


turtle.exitonclick()
