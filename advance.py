from cryptography.fernet import Fernet
import os

# Generate key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print("🔐 File encrypted.")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

    print("🔓 File decrypted.")

# Example usage:
if _name_ == "_main_":
    #Uncomment to test
     generate_key()
     encrypt_file("myfile.txt")
     decrypt_file("myfile.txt")
print("🔧 Tool ready. Uncomment lines to test encrypt/decrypt.")
