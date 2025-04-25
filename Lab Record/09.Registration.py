registered = set(["person1@gmail.com", "person2@gmail.com"])

email = input("Enter your email: ")
if email in registered:
    print("Email already registered.")
else:
    registered.add(email)
    print("Registration successful.")