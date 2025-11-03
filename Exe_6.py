c_password = '12345'
attempt = 0
max_attempts = 5
while attempt < max_attempts:
    password = input("Enter the password: ")
    attempt += 1

    if password == c_password:
        print("Access granted")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempts left")
        else:
            print("Too many incorrect attempts. The authorities have been alerted")