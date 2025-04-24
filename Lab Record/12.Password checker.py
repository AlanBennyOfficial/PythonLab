password = input("Enter a password: ") 

if len(password) < 8: 
    print("Weak password: Too short!") 
elif password.isalpha() or password.isdigit(): 
    print("Weak password: Use a mix of letters and numbers!") 
else: 
    print("Strong password!")