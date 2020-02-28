#!/usr/bin/env python3 

import random

number = random.randint(0,100)
#name = input("Try and guess what number was chosen at random by this app, 0 through 100: ")

while True: 
    user_number = int(input("Guess a number between 0 and 100: "))
    if user_number == number:
        print(f'The number was {number}, you are correct!')
        break
    
    elif user_number > number:
        print(f'The number was {number}, too high of a guess. Next time..')
    
    elif user_number < number:
        print(f'The number was {number}, too low of a guess. Better luck next time..')