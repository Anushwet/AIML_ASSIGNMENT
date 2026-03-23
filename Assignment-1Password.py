
def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_digit:
        return "Password must contain at least one number."
    if not has_special:
        return "Password must contain at least one special character."

    return "Valid"

print("=== Registration ===")
while True:
    password = input("Create a strong password: ")
    result = check_password(password)

    if result == "Valid":
        print("Password created successfully! ✅")
        break
    else:
        print("Error:", result)



print("\n=== Login ===")
attempts = 3

while attempts > 0:
    login = input("Enter your password: ")

    if login == password:
        print("Login Successful! ✅")
        break
    else:
        attempts -= 1
        print("Incorrect Password! Attempts left:", attempts)

if attempts == 0:
    print("Account Locked! ❌")





