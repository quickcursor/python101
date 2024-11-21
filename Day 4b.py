#Day 4 notes
#homework challenge
start = int(input('Pick a number to start with: '))
end = int(input('Pick a number to end with: '))
while start > end or start == end:
    print('Your start number has to be less than your end number.')
    start = int(input('Pick a number to start with: '))
    end = int(input('Pick a number to end with: '))
while start <= end:
    if start % 2 == 0:
        print(str(start) + ' True')
    else: 
        print(str(start) + ' False')
    start += 1

import random
first = int(input('Enter lower number: '))
second = int(input('Enter higher number: '))
number = random.randint(first, second)
guesses = 0
while True:
    guess = int(input('Enter your number: '))
    if guess == number:
        guesses += 1
        print('Correct! Total guesses:' + str(guesses))
        break
    elif guess < first or guess > second:
        print('Invalid Guess')
    elif guess > number:
        guesses += 1
        print('Wrong! it is lower!')
    else:
        guesses += 1
        print('Wrong! It is higher!')

number_of_flips = int(input('Total number of coin flips: '))
heads = 0
tails = 0
extra = number_of_flips
import random
while number_of_flips > 0:
    flip = random.randint(1,2)
    if flip == 1:
        heads += 1
        number_of_flips -= 1
    else:
        tails += 1
        number_of_flips -= 1
Percentage = heads / extra * 100
guess2 = int(input('Guess number of heads: '))
if guess2 == heads:
    print('Correct! Heads: ' + str(heads) + ' Tails: ' + str(tails))
    print('Percentage of Heads: ' + str(Percentage) + '%')
else:
    print('Wrong! Heads: ' + str(heads) + ' Tails: ' + str(tails))
    print('Percentage of Heads: ' + str(Percentage) + '%')