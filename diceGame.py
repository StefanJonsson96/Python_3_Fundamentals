import random

def roll_dice():
    roll = random.randint(1, 6) + random.randint(1,6)
    return roll

player1 = 'Stefan' ##input("Enter player 1's name\n")
player2 = 'Computer' ##input("Enter player 2's name\n")

roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled', roll1)
print(player2, 'rolled', roll2)

if (roll1 > roll2):
    print('You win')
elif (roll1 < roll2):
    print('You loose')
else:
    print('You tie')