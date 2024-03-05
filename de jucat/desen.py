import turtle
import random

t=turtle.Pen()
t.speed(10)
ts=turtle.getscreen()
ts.bgcolor('pink')

colors=["red", "green", "blue","purple","orange","gray"]

for x in range(200):
    t.forward(x) #  ne miscam un pixel
    t.left(60)
    #  t.pencolor(random.choice(colors))
    t.pencolor(colors[x % 6])
    
    
    
    
