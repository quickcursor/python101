number3 = int(input('Enter your number: '))
number4 = 2
prime = True
while True:
    if number3 % number4 == 0:
        prime = False
        break
    else:
        number4 += 1

if prime:
    print(str(number3) + 'is prime.')      
else:
    print(str(number3) + ' is not prime and is divisible by ' + str(number4))