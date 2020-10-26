__author__ = 'dev'

#if elif else
# name = input('1) Please enter your name: ')
# age = int(input('2) Please enter your age:'))
# if(18<age<31):
#     print('welcome to the holiday {}'.format(name))
# elif(18):
#     print('almost {}'.format(name))
# else:
#     print('sorry {}'.format(name))
#====================================================================
# ip addresses challenge
# ip = input('Please enter an ip: ')
# dot = '.'
# noOfSeg = 0
# lengthOfSeg = 0
# e = ''
# for index,e in enumerate(ip):
#
#     if(e in dot):
#         noOfSeg += 1
#         print('Segment {0} has a length of {1}'.format(noOfSeg,lengthOfSeg))
#         lengthOfSeg = 0
#
#     else:
#         lengthOfSeg += 1
# else:
#     if(e != dot):
#         noOfSeg += 1
#         print('Segment {0} has a length of {1}'.format(noOfSeg,lengthOfSeg))
#
# print('Number of Segments: {}'.format(noOfSeg))
#====================================================================
#if else

# import random
#
# highest = 10
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than number
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# WILL BECOME:

# while

import random

highest = 10
answer = random.randint(1, highest)
print("Please guess a number between 1 and {} ".format(highest))
guess = 0
while (guess != answer):
    guess = int(input('Please enter a number: '))
    if guess == 0:
        print("Exiting game")
        break
    elif guess > answer:
        print("Sorry you have not guessed it, Please guess lower")
    elif guess < answer:
        print("Sorry you have not guessed it, Please guess higher")
    else:
        print("Well done, you guessed it,inside")
        break





#====================================================================


