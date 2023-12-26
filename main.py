# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:22:22 2023

@author: aditya
"""


import hangman_words as words
import hangman_art as art
import random


chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

   
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

   
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(art.stages[lives])