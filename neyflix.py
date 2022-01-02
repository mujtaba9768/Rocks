import turtle
t=turtle.Turtle()
t.speed(10)
turtle.bgcolor("white")
t.color("white")
turtle.tile("Netfix Logo made by Mujtaba")
tup()
t.goto(-80,50)
t.down()
t.fillcolor("black")
t.begin_fill()
t.forward(200)
t.setheading(270)
s=360
for i in range(9):
    s=s-10
    t.setheading(s)
    t.forward(10)
