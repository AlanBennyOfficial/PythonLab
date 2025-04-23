balance = 1000 
choice = input("Enter 'D' to deposit, 'W' to withdraw: ").upper() 
 
if choice not in ['D', 'W']: 
    print("Invalid transaction! Please enter 'D' for deposit or 'W' for withdrawal.") 
else: 
    amount = int(input("Enter amount: ")) 
     
    if amount < 0: 
        print("Amount must be positive!") 
    elif choice == 'D': 
        balance += amount 
    elif choice == 'W' and amount > balance:
          print("Insufficient balance!") 
    else: 
        balance -= amount 
 
    print("Updated balance:", balance)