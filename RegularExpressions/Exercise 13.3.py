"""
Author: Neel Srivastava
Date: 17/5/26
Exercise: Regular Expression - Password Validation
Summary: The proram repeadtly asks the user to enter a password and then tells the user if it
is valid or not.
"""

import re

pattern = re.compile(
    r'^'
    r'(?=.*[A-Z])'                 # at least 1 uppercase letter
    r'(?=.*[a-z].*[a-z].*[a-z])'  # at least 3 lowercase letters
    r'(?=.*\d)'                    # at least 1 number
    r'(?=.*[@$!%])'                # at least 1 special character (@$!%)
    r'.{8,}'                       # at least 8 characters total
    r'$'
)

def validate_password(password):
    """Validate a password and print whether it is valid or invalid with feedback."""
    if pattern.match(password):
        print(f"'{password}' is VALID\n")
    else:
        print(f"'{password}' is INVALID")
        if not re.search(r'[A-Z]', password):
            print("  - Missing at least 1 uppercase letter")
        if len(re.findall(r'[a-z]', password)) < 3:
            print("  - Missing at least 3 lowercase letters")
        if not re.search(r'\d', password):
            print("  - Missing at least 1 number")
        if not re.search(r'[@$!%]', password):
            print("  - Missing at least 1 special character (@$!%)")
        if len(password) < 8:
            print("  - Must be at least 8 characters long")
        print()

def main():
    print("Password Validator")
    print("==================")
    print("Rules: 8+ chars, 1+ uppercase, 3+ lowercase, 1+ number, 1+ special char (@$!%)")
    print("Enter Q or q to quit.\n")

    while True:
        password = input("Enter a password: ")

        if password in ('Q', 'q'):
            print("Goodbye!")
            break

        validate_password(password)

if __name__ == "__main__":
    main()



