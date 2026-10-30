# Case Study 29: Password Policy Validation Engine
# Heading: Check Whether a Password Meets Basic Rules

password = input("Enter a sample password: ")

checks = [
    ("At least 8 characters", len(password) >= 8),
    ("Contains uppercase letter",
     any(ch.isupper() for ch in password)),
    ("Contains lowercase letter",
     any(ch.islower() for ch in password)),
    ("Contains a digit",
     any(ch.isdigit() for ch in password)),
    ("Contains special character",
     any(not ch.isalnum() for ch in password))
]

print("\nPassword Validation")

for description, passed in checks:
    if passed:
        print(description + ": Passed")
    else:
        print(description + ": Failed")

if all(passed for description, passed in checks):
    print("Result: Password meets all sample rules.")
else:
    print("Result: Password does not meet all sample rules.")
