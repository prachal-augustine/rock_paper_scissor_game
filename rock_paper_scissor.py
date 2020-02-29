import random


def game_logic():
    if user_choice == 'ROCK' and sys_choice == 'PAPER':
        print('Computer wins')
    elif user_choice == 'PAPER' and sys_choice == 'PAPER':
        print('Its a draw')
    elif user_choice == 'SCISSOR' and sys_choice == 'PAPER':
        print('Congratulations!!! you win')
    elif user_choice == 'ROCK' and sys_choice == 'ROCK':
        print('Its a draw')
    elif user_choice == 'PAPER' and sys_choice == 'ROCK':
        print('Congratulations!!! you win')
    elif user_choice == 'SCISSOR' and sys_choice == 'ROCK':
        print('Computer wins')
    elif user_choice == 'ROCK' and sys_choice == 'SCISSOR':
        print('Congratulations!!! you win')
    elif user_choice == 'PAPER' and sys_choice == 'SCISSOR':
        print('Computer wins')
    elif user_choice == 'SCISSOR' and sys_choice == 'SCISSOR':
        print('Its a draw')


valid_choices = ['ROCK', 'PAPER', 'SCISSOR']
user_choice = ''
sys_choice = ''
while user_choice not in valid_choices:
    user_choice = input("Choose between ROCK, PAPER and SCISSOR \n")
    user_choice = user_choice.upper()
    user_choice = user_choice.strip()
    if user_choice in valid_choices:
        sys_choice = random.choice(valid_choices)
        print("Computer choose: {}".format(sys_choice))
        game_logic()
    elif user_choice == "EXIT":
        print("Bye Bye")
        break
    else:
        print("Please enter a choice among ROCK, PAPER, SCISSOR next time")
