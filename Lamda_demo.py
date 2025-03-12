square = lambda x:x ** 2
print(square(5))


# Map with lambda
lst = [1,2,3,4,5]
squared = list(map(lambda x: x ** 2, lst))
print(squared)