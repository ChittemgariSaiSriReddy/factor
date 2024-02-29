# Password Validator: Develop a program that validates if the entered password meets certain criteria (length, special characters, etc.)


def is_valid_password(password):
    if len(password)<8:
        return False
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    if not (has_upper and has_lower and has_digit):
        return False

    return True

password=input("Enter password :")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")