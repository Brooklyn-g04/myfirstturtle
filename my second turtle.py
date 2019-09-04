import turtle
size = 0



turtle.speed(100)
turtle.color("violet")

def star(turtle):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

        star(turtle)

        for i in range(60):
            star(turtle)Turtle.right(5)
            size += 3