import code
from math import sqrt
from math import hypot
from math import atan2
from math import asin
from math import degrees
import turtle
import random

"""Defining a function that calculates area"""
def area(a=1, b=1, h=1):
    area1 = a*b+(0.5*b*h)
    print(area1)

"""Defining a function that draws a St.Nicholas House"""
def nicholas(x=0, y=0, a=100, b=150, h=50):
    turtle.shape('turtle')
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.left(180 - degrees(asin(h / hypot(0.5 * b,h))))
    turtle.forward(hypot(0.5 * b,h))
    turtle.left(180 - degrees(asin(0.5 * b / hypot(0.5 * b,h))) * 2)
    turtle.forward(hypot(0.5 * b,h))
    turtle.left(90 - degrees(asin(h / hypot(0.5 * b,h))))
    turtle.left(degrees(asin(b / hypot(a,b))))
    turtle.forward(hypot(a,b))
    turtle.left(180 - degrees(asin(b / hypot(a,b))))
    turtle.forward(a)
    turtle.left(90)
    turtle.left(90 - degrees(asin(b / hypot(a,b))))
    turtle.forward(hypot(a,b))
    turtle.left(90)
    turtle.left(90 - degrees(asin(a / hypot(a,b))))
    turtle.forward(b)
    area(a,b,h)


"""Exercise 1"""
area(5, 3, 2)
area(2, 5, 1)
area(3, 3, 3)

a = random.uniform(50, 100)
b = random.uniform(50, 100)
h = random.uniform(50, 100)

nicholas(0, 0, a, b, h)
