import random
import numpy as np

# Define the transition matrix
transition_matrix = np.ones((3, 3)) / 3

# Define the moves
moves = ['rock', 'paper', 'scissors']

# Play the game
while True:
    # Ask the user for their move
    user_move = input("Please enter your choice: ")
    if user_move not in moves:
        print("Invalid move!")
        continue

    # Choose the computer's move based on the transition matrix
    computer_probs = transition_matrix[moves.index(user_move)]
    computer_move = random.choices(moves, weights=computer_probs)[0]

    # Update the transition matrix
    prev_move_index = moves.index(computer_move)
    curr_move_index = moves.index(user_move)
    transition_matrix[prev_move_index, curr_move_index] += 1
    transition_matrix[prev_move_index] /= transition_matrix[prev_move_index].sum()

    # Determine the winner
    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == 'rock' and computer_move == 'scissors') or \
         (user_move == 'paper' and computer_move == 'rock') or \
         (user_move == 'scissors' and computer_move == 'paper'):
        print("You win!")
    else:
        print("You lose!")

    # Ask the user if they want to play again
    play_again = input("Play again? (y/n) ")
    if play_again.lower() != 'y':
        break
