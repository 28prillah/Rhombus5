import turtle

screen = turtle.Screen()
screen.screensize()
screen.bgcolor("yellow")

t=turtle.Turtle()

#moves turtle around screen
t.goto(0,0)
t.setheading(135)
t.fillcolor("cyan")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()


t.goto(0,0)
t.setheading(45)
t.fillcolor("brown")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()


t.hideturtle()


turtle.done()