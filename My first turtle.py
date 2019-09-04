import turtle
turtle.speed(20)


def square(turtle,side):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)



for i in range(60):
    square(turtle,75)
    turtle.left(5)




turtle.exitonclick()