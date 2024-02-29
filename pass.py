import secrets
length = int(input("Enter password length: "))
password = secrets.token_urlsafe(length)

print(password)
