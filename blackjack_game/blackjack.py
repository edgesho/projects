# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:48:34 2024

@author: aditya
"""
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
cards_of_dealer=[]
cards_of_player=[]
def player_cards():
    player=[]
    for i in range(0,2):
        player.append(random.choice(cards))
    return player
def dealer_cards():
    dealer=[]
    dealer.append(random.choice(cards))
    return dealer

def blackjack():
    game_over=False
    while game_over==False:
        choice2=input("do you wish to draw other card?press 'y' for yess and 'n' for no.")
        if choice2=="y":
            game_over=False
            cards_of_player=player_cards()
           
            cards_of_player.append(random.choice(cards))
            
            if 11 in cards_of_player and sum(cards_of_player)>21:
                cards_of_player.remove(11)
                cards_of_player.append(1)
            current_score=sum(cards_of_player)
            print(f"your cards={cards_of_player} current_score={current_score}")
            if current_score>=21:
                final()
                game_over=True
                
        else:
            game_over=True
            final()
            
def final():
    cards_of_dealer=dealer_cards()
    
    while sum(cards_of_dealer)<17:
        cards_of_dealer.append(random.choice(cards))
    if 11 in cards_of_dealer and sum(cards_of_dealer)>21:
        cards_of_dealer.remove(11)
        cards_of_dealer.append(1)
    dealer_score=sum(cards_of_dealer)
    print(f"computers final hand = {cards_of_dealer} computers score={dealer_score}")
    print(compare(sum(cards_of_player),sum(cards_of_dealer)))
    
def compare(user_score,dealer_score):
    if user_score==dealer_score:
        return "Draw"
    elif dealer_score==21:
        return "You loose. opponent wins with a blackjack."
    elif user_score==21:
        return "You win with a blacckjack."
    elif user_score>21:
        return "You went overboard and loose."
    elif dealer_score>21:
        return "Opponent went overboard.You win."
    elif user_score>21 and dealer_score>21:
        return "You loose"
    elif user_score<dealer_score:
        return "You loose."
    else:
        return "You win."
        
choice=input("Do you want to play blackjack? 'y' for yes and 'n' for no.")
if choice=="y":
    cards_of_player=player_cards()
    cards_of_dealer=dealer_cards()
    score=sum(cards_of_player)
    print(f"player cards={cards_of_player}  current_score={score}")
    print(f"dealer cards={cards_of_dealer}")
    blackjack()
    
        