def Fib(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[-1] + lst[-2])
    return lst

n = int(input("Enter the number of elements: "))
print(Fib(n))