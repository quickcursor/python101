#Fahrenheit to Celsius converter
print('This is a Fahrenheit to Celsius converter')
temperature = int(input('What is the temperature in Fahrenheit? '))
celsius = str(int((temperature - 32) * 5/9))
print('The temperature is ' + celsius + ' degrees Celsius' + '!')