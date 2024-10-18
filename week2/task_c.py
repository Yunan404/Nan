password = input("Enter your password: ")
has_letter = False
has_digit = False
if len(password) >= 8:
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
    if has_letter and has_digit:
        print("Your password is valid")
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")

