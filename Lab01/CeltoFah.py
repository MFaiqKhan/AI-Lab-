

# func to convert temp from and to celsius and fahrenheit

def convert_temp(temp, unit):
    if unit == 'c':
        return (temp * 9 / 5) + 32
    elif unit == 'f':
        return (temp - 32) * 5 / 9
    else:
        return 'Invalid unit'

temp = float(input('Enter a temperature: '))
unit = input('Enter the unit (c or f): ')
print(convert_temp(temp, unit))