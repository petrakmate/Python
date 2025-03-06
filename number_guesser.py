import random
# Declaring the number we thought of
n = int(random.randint(1,1000))
g = None
attempts = 0
guessed_correctly = False
print('I thought of a number between 1 and 1000. Try to guess it correctly!')
print('You have 10 guesses.')

while guessed_correctly == False and attempts < 10:
    try:
        # Getting the guess from the user
        g = int(input('Your guess: '))
        attempts += 1
        if g > 1000 or g < 1:
            print('Please enter a number between 1 and 1000.')
        elif g > n:
            print('Lower. {}/10'.format(attempts))
        elif g < n:
            print('Higher. {}/10'.format(attempts))
        else:
            print(f'Correct! Congrats! You guessed the correct number in {attempts} guesses.')
            guessed_correctly = True
    except ValueError:
        'Please try to enter a valid positive number.'

if attempts == 10 and guessed_correctly == False:
    print(f'Unfortunately you ran out of guesses. The number was {n}.')
