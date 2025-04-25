speed = int(input("Enter vehicle speed: ")) 
limit = 60 
 
if speed < 0: 
    print("Speed cannot be negative!") 
elif speed > limit: 
    fine = (speed - limit) * 10 
    print("Over Speeding! Fine is:", fine) 
else: 
    print("No fine. Drive safely!")