from random import randint

# The computer chooses a number from 0 to 10.
computer = randint(0, 10)
print('I am your computer...')
print('I just thought of a number between 0 and 10.')
print('Can you guess which one it was?')

guessed_correctly = False
guesses = 0

# Keep asking until the player gets it right.
while not guessed_correctly:
    guess = int(input('Enter your guess: '))
    guesses += 1

    if guess == computer:
        guessed_correctly = True
    elif guess > computer:
        print('Less... Try again!')
    else:
        print('More... Try again!')

print('You tried {} times. CONGRATULATIONS!!!'.format(guesses))