#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:15:43 2020

@author: jsandeman
"""

import random

options = ['rock', 'paper', 'scissors']
comp_choice_msg = 'The computer chose '
win_msg = 'You win!'
lose_msg = 'You lose!'

while True:
    user_choice = input('Rock, paper, or scissors? ').lower()
    computer_choice = random.choice(options)
    if user_choice not in options:
        break
    else:
        print(comp_choice_msg + computer_choice)
        if computer_choice == user_choice:
            print('You chose the same thing. It\'s a tie!')
        elif user_choice == 'rock':
            if computer_choice == 'paper':
                print('Paper covers rock. ' + lose_msg)
            else:
                print('Rock smashes scissors. ' + win_msg)
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print('Paper covers rock. ' + win_msg)
            else:
                print('Scissors cut paper. ' + lose_msg)
        else:
            #User choice is scissors
            if computer_choice == 'rock':
                print('Rock smashes scissors. ' + lose_msg)
            else:
                print('Scissors cut paper. ' + win_msg)

print('Thanks for playing!')
             