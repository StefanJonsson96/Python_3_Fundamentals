import random


valid_options = ['rock', 'paper', 'scissors']


computer_choise = random.choice(valid_options) 

while True:
    user_choice = input("rock, paper, or scissors?").lower() 

    if user_choice not in valid_options:
        print("Invalid input, please pick rock, paper or scissors.")
        continue

    break

win = 'YOU WIN'
loose = 'YOU LOOSE'
tie = 'YOU TIE'
reason = " because the computer picked " + computer_choise

if computer_choise == user_choice:
    print(tie + reason)
elif user_choice == 'rock' and computer_choise == 'scissors':
    print(win + reason)
elif user_choice == 'paper' and computer_choise == 'rock':
    print(win + reason)
elif user_choice == 'scissors' and computer_choise == 'paper':
    print(win + reason)
else:
    print(loose + reason)