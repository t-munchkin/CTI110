# Using loops, functions, and module import
# 4/26/2022
# CTI-110 P5HW2 - Math Quiz
# Tiffany Burk
#

import random

#
def addRandom():
    n1=random.randint(0,1000)
    n2=random.randint(0,1000)
    print(f'{n1:>6}')
    print(f'+{n2:>5}')
    print('Enter answer')
    ans=int(input())
    while ans!=n1+n2:
        if ans<n1+n2:
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans=int(input('try again:'))
    print('Congratulations!!!! Your answer is correct...')

def subRandom():
    n1=random.randint(0,1000)
    n2=random.randint(0,1000)
    print(f'{n1:>6}')
    print(f'-{n2:>5}')
    print('Enter answer')
    ans=int(input())
    while ans!=n1-n2:
        if ans<n1-n2:
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans=int(input('try again:'))
    print('Congratulations!!!! Your answer is correct..')
if __name__=='__main__':
    
    while 1:

        print('Welcome to Math Quiz!')
        print('MAIN MENU')
        print('--------------------------')
        print('1. Adding Random Numbers')
        print('Subtrcting Random Numbers')
        print('3. Exit')

        num =int(input('Please choose one of the menu options:'))
        if num==3:
            print('Thank you for playing...')
            print('Bye!!')
            break
        if num==1:
            addRandom()
        if num==2:
            subRandom()
