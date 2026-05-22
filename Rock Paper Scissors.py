from random import randint

# Define the game options and choose the computer move.
game_options = ['ROCK', 'PAPER', 'SCISSORS']
computer = randint(0, 2)

print('\033[33mYour options:\033[m \n [ 0 ] ROCK \n [ 1 ] PAPER \n [ 2 ] SCISSORS')
choice = int(input('What is your choice?\n '))

# Show the dramatic countdown and the moves.
print('JO \n KEN \n PO!!!')
print('\033[33m-=\033[m' * 20)
print('The computer played {}'.format(game_options[computer]))
print('The player played {}'.format(game_options[choice]))
print('\033[33m-=\033[m' * 20)

# Determine the winner.
if choice == 1 and computer == 0 or choice == 0 and computer == 2 or choice == 2 and computer == 1:
    print('PLAYER WON!!!')
elif computer == choice:
    print('Draw!!!')
else:
    print('PLAYER LOST!!!')