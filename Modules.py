
import math
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entropy = length * math.log2(len(characters))
    return password

print("Generated Password:", generate_password())
