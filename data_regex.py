import re

def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email))

print(is_valid_gmail("john.doe@gmail.com"))     # True
print(is_valid_gmail("john.doe@yahoo.com"))     # False
print(is_valid_gmail("john!doe@gmail.com"))     # False
