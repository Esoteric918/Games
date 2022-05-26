# simple ROCK, PAPER, SCISSORS game

import random;

choices = ['rock', 'paper', 'scissors'];
computer_choice = random.choice(choices);
print('Welcome to the Rock, Paper, Scissors game!');

while True:
    user_input = input("Please enter your choice: ");
    if user_input == computer_choice:
        print("It's a tie!");
    elif user_input == 'rock':
        if computer_choice == 'paper':
            print("Computer picks paper & covers rock. You lose!");
        else:
            print("You win! Rock breaks scissors.");
    elif user_input == 'paper':
        if computer_choice == 'scissors':
            print("You lose! Scissors cuts paper.");
        else:
            print("You win! Paper covers rock.");
    elif user_input == 'scissors':
        if computer_choice == 'rock':
            print("You lose! Rock breaks scissors.");
        else:
            print("You win! Scissors cuts paper.");

    else: print('Your choice {user_input} is invalid! Please try again.');
    print(f'\nYou entered an {user_input}. The computer chose {computer_choice}.');
    oneMore = input('\nDo you want to play one more time? (y/n) ');
    if oneMore == 'y': continue;
    else: print('\nThank you for playing!\n');
    break;


