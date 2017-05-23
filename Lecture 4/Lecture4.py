# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:45:24 2017

@author: SirTobi92

Lecture 4 Code
"""

counter = 0
def add10(number):
    global counter
    while counter < 10:
        number += 1
        counter = counter + 1
    return number

# Correct Solution
def add10(number):
    counter = 0
    while counter < 10:
        number += 1
        counter = counter + 1
    return number

# Recursion, count to 0
def count_to_0(current):
    if current < 0:
        return
    print(current, end=', ')
    count_to_0(current - 1)

def put_apples(left, right):
    if right == 0:
        return left
    return put_apples(left + 1, right - 1)

print(put_apples(8, 4))

def function(arg0, arg1='default'):
    print(arg0, arg1)
    
function(0, 1)
function(0)
function(arg1=1, arg0=0)

def function(*args):
    print (args)

function(1, 2, 3)

def function(**kwargs):
    print(kwargs)
    
function(arg0=0, mug='tea cup', animal='platypus')

my_fruits = ('apple', 'pear', 'banana')
print(my_fruits[1])
    
for i in range(len(my_fruits)):
    print(my_fruits[i], end=' ')

name = input('What\'s your name? ')
print('Hello ' + name)




