def is_prime(num):
  for x in range( 2, num):
    if (num%x) == 0:
      return False
  return True


x = int(input("Enter the number:"))

if( is_prime(x)):
  print("It is prime")
else:
  print("It is not prime")