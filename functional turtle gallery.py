import turtle
size = 1



turtle.speed(100)
turtle.color("violet")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)

    size += 1.5

turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()


turtle.color("orange")

turtle.speed(20)

size += 1

turtle.speed(20)


turtle.speed(20)


def square(turtle,side):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)



for i in range(72):
    square(turtle,75)
    turtle.left(5)

turtle.penup()
turtle.goto(200, 200)
turtle.pendown()

turtle.speed(100)
turtle.color("light blue")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(72):
    star(turtle, 50)
    turtle.right(5)


turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()



size = 0



turtle.speed(100)
turtle.color("light green")

def square(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(90)

for i in range(80):
    square(turtle, 50)
    turtle.right(5)

    size += 3

turtle.penup()
turtle.goto(100, -100)
turtle.pendown()



turtle.exitonclick()








