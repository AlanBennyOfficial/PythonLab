def square(x):
    for i in range(x):
        yield i**2
    
gen = square(3)
print(list(gen))
    