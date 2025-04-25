t = float(input("Temp: "))

unit = input("°C or °F? ").upper()

if unit == 'C':
    print("°F =", t * 9/5 + 32)
else:
    print("°C =", (t - 32) * 5/9)
