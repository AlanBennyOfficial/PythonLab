square = lambda x:x ** 2
print(square(5))


# Map with lambda
lst = [1,2,3,4,5]
squared = list(map(lambda x: x ** 2, lst))
print(squared)

# Filter with lambda
numbers = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# sorted with lambda
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)
