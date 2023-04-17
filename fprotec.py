#!/usr/bin/python 

# Python File Protection
print("Wellcome to Python File Protection")

from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key=None):
        if key:
            self.key = bytes(key, 'utf-8')
        else:
            self.key = Fernet.generate_key()

    def encrypt_file(self, input_file, output_file):
        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, input_file, output_file):
        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
