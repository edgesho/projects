# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:19:37 2024

@author: aditya
"""
import art
print(art.logo)
def easy_level(x):
    print("You have 10 attempts.")
    attempts=10
    for i in range(1,11):
        number=int(input("enter your choice:"))
        if number<x:
            print("Too low")
            attempts-=1
            print(f"You have {attempts} attempts left.")
        elif number>x:
            print("Too high")
            attempts-=1
            print(f"You have {attempts} attempts left.")
        else:
            print("You have selected the correct number.\nYou Won.!!!")
            break
    if attempts==0:
        print("You loose.")
        print(f"the number was {x}")
        return
    else:
        return
        
        
        
def hard_level(x):
    print("You have 5 attempts.")
    attempts=5
    for i in range(1,6):
        number=int(input("enter your choice:"))
        if number<x:
            print("Too low")
            attempts-=1
            print(f"you have {attempts} attempst left.")
        elif number>x:
            print("Too high")
            attempts-=1
            print(f"You have {attempts} attempts left.")
        else:
            print("You have selected the correct number.\nYou Won.!!!")
            break
    if attempts==0:
        print("You loose.")
        print(f"The number was {x}.")
        return
    else:
        return
        
        
import random
print("Welcome to the number guessing game.!!")
print("I am thinking of a number between 1 to 100.\nCan you guess it?")
x=random.randint(1,101)
level=input("DO you want to play 'easy' or 'hard' level?\n")
if level=="easy":
    easy_level(x)
else:
    hard_level(x)
    

    