# -*- coding: utf-8 -*-
"""
Course: Basic Programming in Python
Exercise 2 of Exercise Sheet 2
"""

import math

#Defining all attacks and damages
def strong_attack_damage(level, strength):
    return math.floor(5 + 1.15 * strength + 0.1 * level)

def normal_attack_damage(level, strength):
    return math.floor(3 + strength + 0.1 * level)

def throw_attack_damage(level, strength):
    return math.floor(10 + 1.2 * strength + 0.1 * level)

def maximum_health(level, defense):
    return math.floor(69 + 3 * level + 28 * defense)

def arrow_damage(agility):
    return math.floor(2+A)

def damage_taken(attack_damage, defense):
    return math.floor(attack_damage * (1.2 - 0.01 * defense) + 0.5)
 
# Assuming that both knights have the same values
strength = 20
level = 31
defense = 30
agility = 7

# defining health level
red_health = math.floor(maximum_health(level, defense) * 0.25)
blue_health = math.floor(maximum_health(level, defense) * 0.20)

#defining attack loop
round = 0
while (red_health > 0) and (blue_health > 0) :
    round = round + 1
    print('Round' + str(round) + ':')
    if red_health > 0 :
        red_attack_damage = 2 * strong_attack_damage(level, strength) + \
                            1 * normal_attack_damage(level, strength)                 
        blue_health = blue_health - damage_taken(red_attack_damage, defense)
    else :
        print ('Red Dead. Blue wins.')
        red_health = 0
        
    if blue_health > 0 :
        blue_attack_damage =    3 * normal_attack_damage(level, strength) + \
                                1 * throw_attack_damage(level, strength)
        red_health = red_health - damage_taken(blue_attack_damage, defense)
    else :
        print ('Blue Dead. Red wins.')
        blue_health = 0
        
    print('Red Health :' + str(red_health))
    print('Blue Health :' + str(blue_health))
    
    




