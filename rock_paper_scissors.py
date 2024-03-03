import random

computer_choise = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("rock, paper, or scissors?")
win = 'YOU WIN'
loose = 'YOU LOOSE'
tie = 'YOU TIE'
reason = "because the computer picked " + computer_choise

if computer_choise == user_choice:
    print(tie + reason)
elif user_choice == 'rock' and computer_choise == 'scissors':
    print(win +  reason)
elif user_choice == 'paper' and computer_choise == 'rock':
    print(win + reason)
elif user_choice == 'scissors' and computer_choise == 'paper':
    print(win + reason)
else:
    print(loose + reason)