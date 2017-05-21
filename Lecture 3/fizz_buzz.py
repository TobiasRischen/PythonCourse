import math

def fizz(number):
    return (number % 3) == 0

def buzz(number):
    return (number % 5) == 0

def fizz_buzz(to):
    number = 1
    while number <= to:
        if fizz(number):
            if buzz(number):
                print ('fizzbuzz')
            else:
                print('fizz')
        else:
            if buzz(number):
                print('buzz')
            else:
                print(str(number))
        number = number + 1

fizz_buzz(100)
