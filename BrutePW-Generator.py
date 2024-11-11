import random
import string

# Define function to generate random passwords
def generate_password(length):
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate 1000 random passwords and save them to a file
with open("", "w") as file:
    for _ in range(1500):
        password = generate_password(random.randint(8, 12))  # Password length between 8 and 12 characters
        file.write(password + "\n")
