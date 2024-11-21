#Day 2 notes
print('Hello world, it\'s Sean again')
mins = int(input('Please Enter the number of minutes: '))
years = mins//(60 * 24 *365)
c = years % (60 * 24 * 365)
days = c//(60 * 24)
print(str(mins) + ' minutes is approximately ' + str(years) + ' years ' + str(days) + ' days!')