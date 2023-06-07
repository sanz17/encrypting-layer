from Crypto.Cipher import AES
import hashlib

# Initialize a secret key for encryption and decryption
key = hashlib.sha256( b'my_secret_key').digest()

# Function to encrypt the data
def encrypt(message):
    iv = b'1234567890123456'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = message + b'\0' * (AES.block_size - len(message) % AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

# Function to decrypt the data
def decrypt(encrypted_message):
    iv = b'1234567890123456'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.rstrip(b'\0')

# Example usage
plaintext_message = b'This is a secret message'
encrypted_message = encrypt(plaintext_message)
decrypted_message = decrypt(encrypted_message)

print("Plaintext message:", plaintext_message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)