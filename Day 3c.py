#LCM Calculator
First = int(input('Enter the first number: '))
Second = int(input('Enter the second number: '))

num = max(First, Second)
while True:
    if num % First == 0 and num % Second == 0:
        break
    else:
        num += 1
print('The LCM of ' + str(First) + ' and ' + str(Second) + ' is ' + str(num))

#HCF Calculator

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

hcf = min(number1, number2)
while True:
    if  number1 % hcf== 0 and number2 % hcf == 0:
        break
    else:
        hcf -= 1
print('The HCF of ' + str(number1) + ' and ' + str(number2) + ' is ' + str(hcf))