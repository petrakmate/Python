import random
# Declaring the number we thought of
n = int(random.randint(1,1000))
g = None
print('I thought of a number between 1 and 1000. Try to guess it correctly!')

while g != n:
    try:
        # Getting the guess from the user
        g = int(input('Your guess: '))
        if g > 1000 or g < 1:
            print('Please enter a number between 1 and 1000.')
        elif g > n:
            print('Lower')
        elif g < n:
            print('Higher')
        else:
            print('Correct! Congrats!')
    except ValueError:
        'Please try to enter a valid number.'