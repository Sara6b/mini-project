import random

print('Welcome to the Rock, Paper, Scissors game!')
choices = ['rock', 'paper', 'scissors']
keep_playing = 'yes'

while keep_playing == 'yes':
    pc_choice = random.choice(choices)
    user_input = input('Please enter your choice from rock, paper or scissors :').lower()
    
    while user_input not in choices:
        print('Error: Input unrecognized. Please enter "rock", "paper", or "scissors".')
        user_input = input('Please enter your choice: ').lower()

    def game(pc_choice, user_input):
        if user_input == pc_choice:
            print('It is a DRAW')
        elif (user_input == 'rock' and pc_choice == 'scissors') or (user_input == 'scissors' and pc_choice == 'paper') or (user_input == 'paper' and pc_choice == 'rock'):
            print('You WON')
        else:
            print('You Lost')

    game(pc_choice, user_input)
    print(f"Computer's choice was: {pc_choice}")
    print(f"Your choice was: {user_input}")

    keep_playing = input('Would you like to keep playing? (yes/no): ').lower()

print('END')

