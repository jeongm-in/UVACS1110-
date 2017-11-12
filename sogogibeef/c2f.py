# version : Jeong Min (sogogibeef)
# c2f.py prompts user to type a temperature in Celsius
# and prints the corresponding temperature in Fahrenheit.

celsius_temperature = float(input('What is the temperature in Celsius? '))
fahrenheit_temperature = (celsius_temperature * 9 / 5.0 + 32)
print('It is %.1f degrees Fahrenheit' % fahrenheit_temperature)
# % .nf : determine which digit to round.
# Source : https://stackoverflow.com/a/455678/8776165
