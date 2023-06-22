import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import base64
from colorama import init as colorama_init
from colorama import Fore, Back, Style
colorama_init()

def textc(color, text):
    return f"{color}{text}{Style.RESET_ALL}"


def derive_key(password):
    """Derive the key from the `password` using the passed `salt`"""
    kdf = Scrypt(salt=b"always", length=32, n=2 ** 14, r=8, p=1)
    return kdf.derive(password.encode())


def generate_key(password):
    """
    Generates a key from a `password` and the salt.
    If `load_existing_salt` is True, it'll load the salt from a file
    in the current directory called "salt.salt".
    If `save_salt` is True, then it will generate a new salt
    and save it to "salt.salt"
    """
    derived_key = derive_key(password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        print("loading file ....")
        file_data = file.read()
    # encrypt data
    print("encrypting....")
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(textc(Fore.LIGHTGREEN_EX, "successfully encrypted"))


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        print("loading file ....")
        encrypted_data = file.read()
    # decrypt data
    try:
        print("decrypting....")
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print(textc(Fore.LIGHTRED_EX, "Invalid token, most likely the password is incorrect"))
        return
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(textc(Fore.LIGHTGREEN_EX, "File decrypted successfully"))
