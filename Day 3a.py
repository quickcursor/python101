print('Welcome to Rock Paper Scissors')
print('1. Rock')
print('2. Paper')
print('3. Scissors')
print('Your current score is 5. If you reach 10, you win. If you get 0, you lose.')
Player = int(input('Select Action(Number): '))
import random
chosen = random.randint(1,3)
points = 5
while points != 10 and points != 0:
    if Player == 1 and chosen == 3:
        print('Computer chose Scissors')
        print('Player wins!')
        points += 1
    elif Player == chosen:
        print('Computer ties with Player!')
    elif Player == 2 and chosen == 1:
        print('Computer chose Rock')
        print('Player wins!')
        points += 1
    elif Player == 3 and chosen  == 2:
        print('Computer chose Paper')
        print('Player wins!')
        points += 1
    elif Player == 1 and chosen == 2:
        print('Computer chose Paper')
        print('Player Lose!')
        points -= 1
    elif Player == 2 and chosen == 3:
        print('Computer chose Scissors')
        print('Player Lose!')
        points -= 1
    else:
        print('Computer chose Rock')
        print('Player Lose!')
        points -= 1
if points == 10:
    print('Player overall win!')
if points == 0:
    print('Player overall Lose!')