import random
print('This is a rock-paper-scissors game.\n'
      'The rules are:\n'
      ' - Rock beats scissors\n'
      ' - Scissors beat paper\n'
      ' - Paper beats rock.\n'
      'You are challenged by the computer. The first one to win two rounds wins the game.\n'
      'You will need to choose a number between 1 and 3 to play.\n')

dict1 = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
c_won = 0
u_won = 0

def match_rps(ci,ui):
    choice_user = dict1[ui]
    choice_computer = dict1[ci]
    if ui in range(1,4):
        if (ui == 1 and ci == 1) or (ui == 2 and ci == 2) or (ui == 3 and ci == 3):
            print(f"{choice_user} vs {choice_computer}")
            print("It's a draw. Try again.")
            computer_won, user_won = 0,0
        elif (ui == 1 and ci == 2) or (ui == 2 and ci == 3) or (ui == 3 and ci == 1):
            print(f"{choice_user} vs {choice_computer}")
            computer_won, user_won = 1,0
            print('Computer won this round.')
        else:
            print(f"{choice_user} vs {choice_computer}")
            computer_won, user_won = 0,1
            print('You won this round.')
    else:
        print('----------\n'
              'Please enter a number from 1 to 3 to play.')
        computer_won, user_won = 0, 0
    return computer_won, user_won

while c_won < 2 and u_won < 2:
    # declaring the computer choice
    computer_random_int = random.randint(1, 3)
    # getting the user's choice
    try:
        user_int = int(input('1 - Rock, 2 - Paper, 3 - Scissors\n'
                         'Enter your choice: '))
        if user_int in range(1,4):
            result_c, result_u = match_rps(computer_random_int, user_int)
            c_won = c_won + result_c
            u_won = u_won + result_u
            print(f'{u_won}-{c_won}')
            print('----------')
        else:
            print('----------\n'
                  'Please enter a number from 1 to 3 to play.')
    except ValueError:
        print('----------\n'
              'Please enter a number from 1 to 3 to play.')

if u_won == 2:
    print('You won the game! Congratulations!')
elif c_won == 2:
    print('You lost :( Better luck next time!')
else:
    print('Game finished')