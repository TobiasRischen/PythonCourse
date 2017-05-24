# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:44:54 2017

@author: SirTobi92
"""

with open('lottery.txt', \
          'r') as lottery_file:
    lottery_raw = lottery_file.read()
    # This is black python magic! Let's discuss it
numbers = [int(num) for num in \
           lottery_raw[1:-1].split(',')]
print(numbers)
print(type(numbers))

a = str([1, 2, 3])
b = [int(num) for num in a[1:-1].split(',')]
print(b)
print(type(b))

# conversion from string to num-list
c = []
reduced_a = a[1:-1]
split_a = reduced_a.split(',')
for num in split_a:
    c.append(int(num))
    
print(c)
print(type(c))


