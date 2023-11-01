# -*- coding: utf-8 -*-
'''
[Graf algoritmi]: Vjezba 2 - Zadatak 4

Simulirati igru ”kamen, škare, papir”. Igrač igra protiv kompjutera. Igrač
bira jedno od ta tri pojma i dobija bod u svakom krugu ukoliko ima jači
alat. Pravila su:
· kamen pobjeđuje škare
· škare pobjeđuju papir
· papir pobjeđuje kamen
Koristiti containere za definiranje pravila igre.

@author Anamarija Papic
'''

# Python core built-in containers are:
# lists, tuples, dictionaries, and sets

import random

def validate_user_input(message, min_value, max_value):
    while True:
        choice = int(input(message))
        if min_value <= choice <= max_value:
            return choice
        else:
            print('Wrong input! Please retry.')

def game():
    options = {
        1: 'rock',
        2: 'paper',
        3: 'scissors'
    }

    winning_choices = [
        (1, 3), # rock > scissors
        (3, 2), # scissors > paper
        (2, 1)  # paper > rock
    ]

    points = validate_user_input('Enter how many points must be scored to win a game: ', 1, 100)
    print(f'The first side to score {points} points wins the game.')
   
    user_points = 0
    computer_points = 0
   
    round_number = 1
   
    while user_points < points and computer_points < points:
        print(f'\n--- Round #{round_number} ---')
       
        for key, value in options.items():
            print(f'{key} - {value}')
       
        user = validate_user_input('Enter your choice: ', 1, len(options))
        computer = random.randint(1, len(options))
       
        print(f'You: {options[user]}\tComputer: {options[computer]}')
       
        if user == computer:
            print('Draw!')
        elif (user, computer) in winning_choices:
            print('You win!')
            user_points += 1
        else:
            print('Computer wins!')
            computer_points += 1
       
        print(f'--- Points ---\nYou: {user_points}\tComputer: {computer_points}')
       
        if user_points == points:
            print('\nCongrats! You won the game!')
        elif computer_points == points:
            print('\nGame over! Computer won the game!')
        else:
            round_number += 1

game()
