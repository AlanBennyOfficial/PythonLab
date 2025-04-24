import random
user = input("R/P/S: ").upper()

if user not in ['R','P','S']:
    print("Invalid input! Please enter R, P, or S.")
    exit()
    
comp = random.choice(['R','P','S'])
print("Computer:", comp)
if user == comp:
    print("Tie")
elif (user,comp) in [('R','S'),('S','P'),('P','R')]:
    print("You win")
else:
    print("You lose")
