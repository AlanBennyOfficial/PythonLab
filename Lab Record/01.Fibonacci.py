# Print first n Fibonacci numbers
n = int(input("No of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
