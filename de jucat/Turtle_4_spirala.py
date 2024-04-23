import turtle
import random

t=turtle.Pen()
t.speed(10)
ts=turtle.getscreen()
ts.bgcolor('pink')

colors=["red", "green", "blue","purple","orange","gray"]

for x in range(200):
    t.backward(2*x) 
    t.left(121)

    
