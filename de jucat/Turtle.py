import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(5)
t.speed(25)
col = ("magenta", "yellow", "green", "blue")
for i in range(200):
    t.pencolor(col[i%4])
    t.forward(i*5)
    t.left(121)
    t.circle(10.0)
    t.pensize(1)
turtle.Terminator()
