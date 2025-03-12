numbers = [1, 2, 3, 4, 5]
exponent = [1, 2, 3, 4, 5]
powered = list(map(pow, numbers, exponent))
print(powered)

# Map function with custom function
custom = list(map(lambda x, y: x + y, numbers, exponent))
print(custom)