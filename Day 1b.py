#interest calculator
print('Calculate your bank interest!')
deposit = int(input('What is your deposit? '))
years = int(input('How many years are you leaving this in the bank? '))
final = str(int(deposit * (1.02 ** years) + 1))
print('Your final amount will be ' + '$' + final + '!')