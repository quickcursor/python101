NRIC = int(input('Enter your NRIC number: '))
Day = int(input('Enter your desired day:(Monday = 1, Tuesday = 2...) '))
if NRIC % 2 == Day % 2:
    print('It is allowed!')
else:
    print('It is not allowed!')

money = int(input('Enter stored amount in $: '))
expiry = int(input('Enter expiry year: '))
if money > 100 and expiry >= 2024:
    print('This card that expires in ' + str(expiry) + ' is valid!')
if money > 100 and expiry < 2024:
    print('This card that expires in ' + str(expiry) + ' is not valid!')
if money <= 100 and expiry >= 2024:
    print('This card that has less than $100 is not valid!')
if money <= 100 and expiry < 2024:
    print('This card that expires in ' + str(expiry) + ' and has less than $100 is not valid!')