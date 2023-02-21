def check_password():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if password.lower() == "abc$123":
        return f"Welcome!, {username}"
    else:
        return "I don't know you."


result = check_password()
print(result)