import re

# Patterns
name_pattern = r"^[A-Z][a-zA-Z]{2,}$"
email_pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
phone_pattern = r"^\+\d{1,3} \d{10}$"
password_pattern = r".{8,}"


class InvalidInput(Exception):
    pass

def validate_name(first_name, last_name):
    if not (re.match(name_pattern, first_name) and re.match(name_pattern, last_name)):
        raise InvalidInput("First and last names must start with a capital letter and be at least 3 characters long.")
    return f"{first_name} {last_name} is a valid name."

def validate_email(email):
    if not re.match(email_pattern, email):
        raise InvalidInput("Email should be in the format: abc.xyz@bl.com")
    return f"{email} is a valid email."

def validate_phone(phone):
    if not re.match(phone_pattern, phone):
        raise InvalidInput("Phone number should be in the format: +91 9876543210")
    return f"{phone} is a valid phone number."

def validate_password(password):
    if not re.match(password_pattern, password):
        raise InvalidInput("Password must be at least 8 characters long.")
    return f"Password is valid."

if __name__ == "__main__":
    try:
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        email = input("Enter the email: ")
        phone = input("Enter the phone number (e.g., +91 9876543210): ")
        password = input("Enter the password: ")
        
        # Validation
        print(validate_name(first_name, last_name))
        print(validate_email(email))
        print(validate_phone(phone))
        print(validate_password(password))

    except InvalidInput as e:
        print(e)
