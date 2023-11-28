import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Password length should be greater than zero.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

#if name == "main":
main()