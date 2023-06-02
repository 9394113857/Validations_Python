import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\d{10}$'  # Updated pattern for 10-digit Indian phone number
    return re.match(pattern, phone) is not None

email_valid = False
phone_valid = False

while not email_valid:
    email = input("Enter an email address: ")
    if validate_email(email):
        email_valid = True
        print("Email is valid.")
    else:
        print("Email is invalid. Please try again.")

while not phone_valid:
    phone = input("Enter a phone number (10 digits in Indian format): ")
    if validate_phone(phone):
        phone_valid = True
        print("Phone number is valid.")
    else:
        print("Phone number is invalid. Please try again.")

# Print the final results
print("\nFinal Results:")
print("Email:", email)
print("Phone number:", phone)
