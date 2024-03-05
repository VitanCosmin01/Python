#rozeta 
import turtle

t=turtle.Pen()
t.speed(20)
ts=turtle.getscreen()
#ts.bgcolor('pink')
t.pensize(8)

colors=["red","green","blue","purple","orange","gray","yellow","magenta","pink","brown","silver","gold"]

for x in range(30):
    t.circle(60)
    t.left(40)
    t.pencolor(colors[x%12])
