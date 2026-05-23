# Basic encryption and decryption

# Modules
import random
import string

# Variables
chars = " " +string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter the plaintext: ")
cipher_text = ""

# Encryption
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"Encrypted text: {cipher_text}")

# Decryption
cipher_text = input("Enter the ciphertext: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"Decrypted text: {plain_text}")
