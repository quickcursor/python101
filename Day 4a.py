#banking app!
import time
import random
print('Welcome to QWERTY Bank! What would you like to do?')
print('You have to create an account. In an account, you start with $1000.' )
print('Every year, we will update your account with our interest.Your current interest rate per year is 9%.')
print('You advance one year after depositing and withdrawing your money at least 10 times!')
account1 = 1000
wrong = 0
advance = 0
interest_rate = 0.09
while True:
    print('1. Deposit money')
    print('2. Withdraw money')
    print('3. End')
    print('4. Create account')
    print('5. Change PIN')
    print('6. Test your luck in a guessing game!')
    print('7. Calculate interest')
    if wrong == 3:
        print('You have been locked out!')
        while account1 > 0:
            account1 -= 1
            time.sleep(0.05)
            print('Updated balance: $' + str(account1))
    if advance == 10:
        print('You advance 1 year!')
        extra = account1 * (1 + interest_rate)
        extra = int(extra)
        print('Updated Balance: ' + str(extra))
        account1 = extra
        advance = 0
    option = int(input('Choose your option: '))
    if option == 3:
        break
    elif option == 2:
        while wrong < 3:
            check = int(input('Please enter your PIN: '))
            if check == PIN:
                print('Correct! You may pass.')
                withdraw = int(input('Enter withdraw amount: '))
                if withdraw > account1:
                    print('Insufficient Balance!')
                    print('Updated Balance: ' + str(account1))
                    break
                else:
                    account1 -= withdraw
                    print('Updated Balance: ' + str(account1))
                    advance += 1
                    break
            else:
                print('Wrong!')
                wrong += 1
    elif option == 1:
        while wrong < 3:
            check = int(input('Please enter your PIN: '))
            if check == PIN:
                print('Correct! You may pass.')
            else:
                print('Wrong!')
                wrong += 1
                break
            deposit = int(input('Enter Deposit Amount: '))
            account1 += deposit
            print('Updated Balance: ' + str(account1))
            advance += 1
            break
    elif option == 4:
        import random
        PIN = random.randint(100000, 999999)
        print('Your PIN is ' + str(PIN))
    elif option == 5:
        test2 = int(input('What is your current PIN? '))
        if test2 == PIN:
            test3 = int(input('What would you like your new PIN to be?(Needs to be a number)'))
            PIN = int(input('Please retype your new PIN. '))
            if test3 == PIN:
                print('Your new PIN is: ' + str(PIN))
        else:
            wrong += 1
            break
    elif option == 6:
        print('In this game, you choose a range between 1 and 10. If you guess it in:')
        print('1 try, you get $15')
        print('2 tries, you get $10')
        print('3 tries, you get $5')
        print('Otherwise, your interest per year will decrease by 0.1%.')
        number = random.randint(1, 10)
        guesses = 0
        while True:
            guess = int(input('Enter your number: '))
            if guess == number:
                guesses += 1
                print('Correct! Total guesses:' + str(guesses))
                if guesses == 1:
                    print('Congratulations! You win $15')
                    print('Your interest rate per year has increased by 0.01%')
                    account1 += 15
                    interest_rate += 0.01
                    print('Updated amount: $' + str(account1))
                    break
                elif guesses == 2:
                    print('Congratulations! You win $10')
                    account1 += 10
                    interest_rate += 0.01
                    print('Updated amount: $' + str(account1))
                    break
                elif guesses == 3:
                    print('Congratulations! You get $5!')
                    account1 += 5
                    interest_rate += 0.01
                    print('Updated amount: $' + str(account1))
                    break
                else:
                    print('Sorry! Better luck next time!')
                    print('Your interest rate per year has decreased by 0.01%')
                    interest_rate -= 0.01
                break
            elif guess < 1 or guess > 10:
                print('Invalid Guess')
            elif guess > number:
                guesses += 1
                print('Wrong! it is lower!')
            else:
                guesses += 1
                print('Wrong! It is higher!')
    elif option == 7:
        print('We have two types of calculators.')
        print('1. Calculate your money at the end of a number of years!')
        print('2. Calculate the number of years it takes for you to reach a desired amount of money!')
        option2 = int(input('Please choose your option: '))
        if option2 == 1:
            rate = float(input('What is your interest rate per year?'))
            years = int(input('How many years are you leaving your money in the bank?'))
            initial = int(input('What is your current amount in $? '))
            final = initial * (rate + 1) ** years
            final = int(final)
            print('Your final amount will be: $' + str(final) + '!')
            break
        else:
            desired_final = int(input('What is your desired final amount? '))
            initial2 = int(input('What is your current amount? '))
            rate2 = float(input('What is your interest rate? '))
            count = 0
            while initial2 < desired_final:
                initial2 *= (rate2 + 1)
                count += 1
            print('It would take you ' + str(count) + ' years!')
            break
    else:
        print('Invalid option.')