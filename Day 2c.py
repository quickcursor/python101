#Concept: elif
# score = int(input('Enter your score here: '))
import random
score = int(random.randint(0,100))

if score > 100 or score < 0:
    print('Invalid Score')
elif score > 90:
    print(str(score) + ' is A.')
elif score >= 81:
   print(str(score) + ' is B.')
elif score >= 71:
    print(str(score) + ' is C.')
elif score >= 61:
    print(str(score) + ' is D.')
else:
    print(str(score) + ' is E.')