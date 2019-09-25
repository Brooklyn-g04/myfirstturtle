import turtle

Ross = turtle.Turtle()
Rachel = turtle.Turtle()
Chandler = turtle.Turtle()
Monica = turtle.Turtle()
Phoebe = turtle.Turtle()

Ross.shape("turtle")
Rachel.shape("turtle")
Chandler.shape("turtle")
Monica.shape("turtle")
Phoebe.shape("turtle")

Ross.fillcolor("green")
Ross.begin_fill()
Ross.color("green")
Ross.forward(800)
Ross.backward(1800)
Ross.right(90)
Ross.forward(800)
Ross.left(90)
Ross.forward(1800)
Ross.left(90)
Ross.forward(800)
Ross.end_fill()

Rachel.fillcolor("pink")
Rachel.begin_fill()
Rachel.color("pink")

def square(turtle,side):
    for i in range(4):
        Rachel.right(90)
        Rachel.forward(100)

Rachel.right(180)


square(turtle, 75)
Rachel.right(90)
Rachel.forward(100)
Rachel.end_fill()

Rachel.fillcolor("purple")
Rachel.begin_fill()
Rachel.right(35)
Rachel.forward(100)
Rachel.right(117)
Rachel.forward(98)
Rachel.end_fill()

Chandler.forward(300)

Chandler.circle(15)
Chandler.forward(100)
Chandler.circle(15)

Chandler.left(90)
Chandler.penup()
Chandler.forward(30)
Chandler.pendown()
Chandler.right(90)
Chandler.forward(20)
Chandler.left(90)
Chandler.forward(100)
Chandler.left(90)
Chandler.forward(200)
Chandler.left(90)
Chandler.forward(100)
Chandler.left(90)
Chandler.forward(200)
Chandler.left(90)
Chandler.forward(75)
Chandler.right(90)
Chandler.forward(40)
Chandler.right(90)
Chandler.forward(70)
Chandler.right(90)
Chandler.forward(40)
Chandler.right(180)

turtle.exitonclick()