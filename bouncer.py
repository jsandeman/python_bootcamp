#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 05:33:37 2020

@author: jsandeman
"""

try:
    age = int(input('How old are you? '))
    if age > 17:
        print('Okay, you can enter the concert.')
        if age > 20:
            print('And here\'s a bracelet so you can order booze.')
    else:
        print('Sorry, you need to be at least 18 years old to attend this event.')
except:
    print('Don\'t you try and bullshit me, punk! Get outta here!')

