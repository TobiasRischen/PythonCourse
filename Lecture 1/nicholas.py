import code
from math import sqrt
from math import hypot
from math import atan2
from math import degrees
import turtle
import random

"""Defining a function that draws a St.Nicholas House"""
def nicholas(x=0,y=0,a=10,b=10,h=10):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.left(90+45)
    turtle.forward(sqrt(0.5*h*0.5*h*2))
    turtle.left(90)
    turtle.forward(sqrt(0.5*h*0.5*h*2))
    turtle.left(45)
    turtle.left(degrees(atan2(a,b)))
    turtle.forward(hypot(a,b))
    turtle.left(180-degrees(atan2(a,b)))
    turtle.forward(a)
    turtle.left(90)
    turtle.left(90-degrees(atan2(a,b)))
    turtle.forward(hypot(a,b))
    turtle.left(90)
    turtle.left(degrees(atan2(a,b)))
    turtle.forward(b)

"""Exercise 1"""
turtle.shape('turtle')
nicholas(0,0,100,100,100)

"""Fun"""
turtle.speed(500)
for i in range(1,51):
    nicholas(-250+i*10,-100,10,12)

code.interact()
