# Version : Jeong Min Lim (sogogibeef)
# conversion.py has two functions c2f and f2c
# that respectively converts temperature in Celsius and Fahrenheit

def c2f(temp_in_celsius):
    celsius_to_fahrenheit = temp_in_celsius / 5 * 9 + 32
    return celsius_to_fahrenheit

def f2c(temp_in_fahrenheit):
    fahrenheit_to_celsius = (temp_in_fahrenheit -32)* 5 / 9
    return fahrenheit_to_celsius

