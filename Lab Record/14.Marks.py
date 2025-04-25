def calculate_grade(marks): 
    average = sum(marks) / len(marks) 
    if average >= 90: 
        return 'A' 
    elif average >= 75: 
        return 'B' 
    elif average >= 50: 
        return 'C'
    else: 
        return 'F'

marks = [] 
for i in range(3): 
    mark = int(input(f"Enter marks for subject {i+1} (0-100): ")) 
    if 0 <= mark <= 100: 
        marks.append(mark) 
    else: 
        print("Marks should be between 0 and 100.") 
        exit() 
print("Grade:", calculate_grade(marks))