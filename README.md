# Proteksi File

Proteksi File is a Python module that provides file encryption and decryption capabilities using the Fernet encryption algorithm from the `cryptography` package.

## Installation

To use the Proteksi File module, you need to have Python 3.x and the `cryptography` package installed on your system. You can install the `cryptography` package using pip:

'''pip install cryptography'''


You can then download the `fprotec.py` file from this repository and use it in your Python program.

## Usage

To use the Proteksi File module, you need to create an instance of the `FileEncryptor` class and specify a key to use for encryption and decryption. You can then call the `encrypt_file()` and `decrypt_file()` methods to encrypt and decrypt files, respectively.

Here's an example usage:

'''python
from file_encryptor import FileEncryptor

## create a new file encryptor with a custom key
key = 'This is a custom key'
encryptor = FileEncryptor(key=key)

## encrypt a file using the custom key
encryptor.encrypt_file('input.txt', 'encrypted.txt')

## decrypt the encrypted file using the custom key
encryptor.decrypt_file('encrypted.txt', 'decrypted.txt')
'''

The encrypt_file() method takes two parameters: the path to the input file and the path to the output file. The method reads the contents of the input file, encrypts the data using the Fernet encryption algorithm with the specified key, and writes the encrypted data to the output file.

The decrypt_file() method takes two parameters: the path to the input file and the path to the output file. The method reads the encrypted data from the input file, decrypts the data using the Fernet encryption algorithm with the specified key, and writes the decrypted data to the output file.

By default, if no key is specified when creating a FileEncryptor instance, a random key is generated using the generate_key() method provided by Fernet.

# Security Considerations

It's important to keep the encryption key secret and stored securely. Anyone with access to the key can decrypt the encrypted data. If the key is compromised, all data encrypted with that key is also compromised.

# License

This module is licensed under the MIT License. See the LICENSE file for details.
