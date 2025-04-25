tasks = []

def add(task):    
    tasks.append(task)

def view():       
    [print(f"{i+1}. {t}") for i,t in enumerate(tasks)]

def clear():      
    tasks.clear()

while True:
    cmd = input("[A]dd/[V]iew/[C]lear/[Q]uit: ").upper()
    if   cmd == 'A': add(input("Task: "))
    elif cmd == 'V': view()
    elif cmd == 'C': clear()
    elif cmd == 'Q': break
    else:            print("Invalid command.")
