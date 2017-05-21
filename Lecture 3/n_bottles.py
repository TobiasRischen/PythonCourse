import math

def n_bottles(n):
    if (n > 99) or (n < 5):
        print('I want to sing a funnier song than ' + str(n) + ' bottles.')
        n = 0
    else:
        while n > 0:
            if n == 1:
                print(str(n) + ' bottle of beer on the wall, ' + str(n) + ' bottle of beer.')
                n = n - 1
                print('Take one down and pass it around, no more bottles of beer on the wall.')
            else:
                print(str(n) + ' bottles of beer on the wall, ' + str(n) + ' bottles of beer.')
                n = n - 1
                print('Take one down and pass it around,' + str(n) + ' bottles of beer on the wall.')


n_bottles(100)
n_bottles(4)
n_bottles(99)
