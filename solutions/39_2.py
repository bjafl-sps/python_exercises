# -*- coding:utf-8 -*-
'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20.
(Source: http://inventwithpython.com) This is how it should work when run in a terminal:
>>> import guess_number
Hello! What is your name?
Torbjørn
Well, Torbjørn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjørn! You guessed my number in 3 guesses!
'''
#Method 2 using recursion. Here global makes count available to local scope of your function.
import random

def check():
    global count  
    guess = int(input("Take a guess\n"))
    if guess == no:
        print("Good job, %s! You guessed my number in %d guesses!" %(name,count))
    if guess < no:
        print("Your guess is too low.")
        count +=1        
        check()          
    if guess > no:
        print("Your guess is too high")
        count +=1
        check()

name = input("Hello! What is your name?\n")
print("Well, " + name + ", I am thinking of a number between 1 and 20")
no = random.randint(1,20)
count  =1
check()