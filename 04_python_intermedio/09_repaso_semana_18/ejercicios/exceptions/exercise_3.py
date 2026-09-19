
def input_user():
    # Username:
    attempts = 3

    while attempts > 0:
        try:
            username = input("Username: ")

            if not 3 <= len(username) <= 20:
                raise ValueError("Error: Username must be between 3 and 20 characters long")
            
            if not username.replace("_","").isalnum():
                raise ValueError("Error: Username can only contain letters, numbers and underscores")
            
            break
        
        except ValueError as e:
            attempts -= 1
            print(str(e))
            print(f"Attempts left: {attempts}")

    if attempts == 0:
        raise RuntimeError("Too many failed attempts")

    # Email:
    attempts = 3

    while attempts > 0:
        try:
            email = input("Email: ")

            if email.count("@") != 1:
                raise ValueError("Error: @ missing")
            
            local, domain = email.split("@")

            if "." not in domain:
                raise ValueError("Error: Your domain is missing a dot (.)")
            
            break

        except ValueError as e:
            attempts -= 1
            print(str(e))
            print(f"Attempts left: {attempts}")

    if attempts == 0:
        raise RuntimeError("Too many failed attempts")
    
    # Age:
    attempts = 3

    while attempts > 0:
        try:
            age = int(input("Age: "))

            if not 13 <= age <= 120:
                raise ValueError("Error: Please enter a valid age (13-120)")
        
            break

        except ValueError as e:
            attempts -= 1
            print(str(e))
            print(f"Attempts left: {attempts}")
    
    if attempts == 0:
        raise RuntimeError("Too many failed attempts")
    
    # Password:
    attempts = 3

    while attempts > 0:
        try:
            password = input("Password: ")

            if len(password) < 8:
                raise ValueError("Error: The password must be at least 8 characters long")

            if not any(char.isdigit() for char in password):
                raise ValueError("Error: The password must contain at least one (1) number")
            
            break
        
        except ValueError as e:
            attempts -= 1
            print(str(e))
            print(f"Attempts left: {attempts}")

    if attempts == 0:
        raise RuntimeError("Too many failed attempts")

    return username, email, age, password


def main():
    try:
        result = input_user()
    except RuntimeError as e:
        print(str(e))
        return
    
    username, email, age, password = result

    print("\nRegistration complete:")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Password: {password}")


main()