fahrenheit_temps = [32, 68, 77, 104, 50]
print("Temperatures in Fahrenheit:", fahrenheit_temps)
celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]
print("Temperatures in Celsius:", celsius_temps)
