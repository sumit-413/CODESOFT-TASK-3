import random
import string

print("PASSWORD GENERATOR")
try:
    length = int(input("Enter the desired password length: "))
except ValueError:
    print("Please enter a valid number!")
    exit()

letters = string.ascii_letters      
digits = string.digits             
symbols = string.punctuation       
all_characters = letters + digits + symbols


if length < 4:
    print("Password should be at least 4 characters long.")
else:
    password = ''.join(random.choice(all_characters) for _ in range(length))

    print("\n Generated Password:")
    print(password)