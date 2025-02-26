lst = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    a = input(f"Enter the element {i}: ")
    lst.append(a)

print("Add a new member \n")
lst.append(input("Add a list member: "))
print(lst)

lst.sort()
print("Sorted list:")
print(lst)

lst.sort(reverse=True)
print("Reversed list:")
print(lst)

x = int(input("Enter the element index to be removed: "))
lst.pop(x)
print(lst)
