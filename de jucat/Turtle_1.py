# import turtle as tur
# import colorsys as cs
# tur.setup(800,800)
# tur.speed(0)
# tur.width(2)
# tur.bgcolor("black")
# for j in range(25):
#     for i in range(15):
#         tur.color(cs.hsv_to_rgb(i/15, j/25,1))
#         tur.right(90)
#         tur.circle(200-j*4,90)
#         tur.left(90)
#         tur.circle(200-j*4,90)
#         tur.right(180)
#         tur.circle(50,24)
# tur.hideturtle()
# tur.done()
#

import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(100)






# # Python Programmer Club, [08.06.2023 04:00]
# from turtle import *
# import turtle as t
#
# def my_turtle():
#     # Choices
#     sides = str(3)
#     loops = str(450)
#     pen = 1
#     for i in range(int(loops)):
#         forward(i * 2/int(sides) + i)
#         left(360/int(sides) + .350)
#         hideturtle()
#         pensize(pen)
#         speed(30)
#
# my_turtle()
# t.done()
