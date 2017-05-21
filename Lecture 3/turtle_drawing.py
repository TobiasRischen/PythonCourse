import code
import math
from math import sqrt
from math import hypot
from math import atan2
from math import asin
from math import degrees
import turtle
import random

"""Defining a function that draws a St.Nicholas House"""
def nicholas(h=10):
    a = 2/3 * h
    b = 2/3 * a
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

"""Defining a function that draws a Tree"""
def draw_tree(h=20):
    turtle.left(90)
    if h != 0:
        turtle.forward(h)
        draw_tree_arms(h)
        turtle.backward(h)

"""Defining a function that draws a a tree's arms"""
def draw_tree_arms(h):
    turtle.left(30)
    turtle.forward(h / 1.5)
    if h > 20:
        draw_tree_arms(h / 1.5 / 1.5) # decide whether large tree
    turtle.backward(h / 1.5)
    turtle.right(2 * 30)
    turtle.forward(h / 1.5)
    if h > 20:
        draw_tree_arms(h / 1.5 / 1.5)  # decide whether large tree
    turtle.backward(h / 1.5)
    turtle.left(30)

"""Defining a function that draws a flat world"""
def flatworld(x=5, h=40):
    distance_to_tree = h * 1/2 * 2/3 * 2/3 * 1/2
    house_length = h * 1/2 * 2/3 * 2/3
    length_of_world = house_length * x + distance_to_tree * x * 2
    start_point = (-1) * length_of_world / 2
    turtle.shape('turtle')
    turtle.penup()
    turtle.setpos(start_point,0)
    turtle.pendown()
    counter = 0
    while x > 0:
        nicholas(h / 2)
        turtle.penup()
        turtle.forward(distance_to_tree)
        turtle.pendown()
        draw_tree(h)
        turtle.right(90)
        turtle.penup()
        turtle.forward(distance_to_tree)
        turtle.pendown()
        x = x - 1

flatworld(10,50)
