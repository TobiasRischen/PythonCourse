# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:30:45 2017

@author: SirTobi92
"""

"""
Exercise 1
"""
# too hard
"""
Exercise 2: Hangman
"""
import math
import random

def open_file(filename):
    with open(filename, 'r') as wordlist:
        return wordlist.read().splitlines()

def pick_word(list):
    return str(random.choice(list))


def create_guess_word(given_word):
    for i in range(0,len(given_word)):
        guess_word.append('_')
        check_word.append(str(given_word[i]))

def update_guess_word(given_word,guess_word_list,check_word_list,given_letter):
    for i in range(0,len(given_word)):
        if check_word_list[i] == given_letter:
            guess_word_list[i] = given_letter
        

number_of_misses = 5

wordlist = open_file('hangman_words.txt')

word = pick_word(wordlist)


fail_list = []
guess_word = []
check_word = []
create_guess_word(word)

rules = """Here are the rules."""
print(rules)

while check_word != guess_word and number_of_misses > 0:
    print('Here is your word:')
    print(guess_word)
    print('Here is your list of fails:')
    print(fail_list)
    print('You have ' + str(number_of_misses) + ' misses left until you hang.')
    next_letter = input('What is your next guess? ')
    print('Your guess was "' + str(next_letter) + '".')
    if next_letter in word:
        update_guess_word(word,guess_word,check_word,next_letter)
        if check_word == guess_word:
            print("Congrats. You won. And you did not hang :-)")
            print(check_word)
    else:
        fail_list.append(next_letter)
        number_of_misses = number_of_misses - 1
        if number_of_misses == 0:
            print("No misses left. You hang.")





    