# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:12:00 2024

@author: aditya
"""

import game_data as gd
import art
import random
game_lost=False
score=0
while game_lost==False:
    print(art.logo)
    
    A=random.choice(gd.data)
    print(f"A:{A['name']} {A['description']} {A['country']}")
    print(art.vs)
    B=random.choice(gd.data)
    print(f"B:{B['name']} {B['description']} {B['country']}")
    guess=input("which has higher followers A or B?")
    if guess=="A":
        if A['follower_count']>B['follower_count']:
            print("Correct answer.")
            score+=1
            print(f"Your score is {score}")
            game_lost=False
        else:
            print("Wrong answer.")
            game_lost=True
    else:
        if A['follower_count']<B['follower_count']:
            print("Correct answer.")
            score+=1
            print(f"Your score is {score}")
            game_lost=False
        else:
            print("Wrong answer.")
            game_lost=True
        
print(f"Your score is {score}.")   
    
    



