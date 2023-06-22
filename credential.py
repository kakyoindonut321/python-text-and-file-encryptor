import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import base64
import ast


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


def add_credential(key, variable, value):
    credential_path = "credentials.txt"
    credential = open(credential_path, "rb").read()
    f = Fernet(generate_key(key))
    try:
        if credential:
            decrypted_data = f.decrypt(credential)
            credit_dictionary = ast.literal_eval(decrypted_data.decode())
            credit_dictionary.update({variable: value})

            encrypted_data = f.encrypt(str(credit_dictionary).encode())
            credit_write = open(credential_path, "wb")
            credit_write.write(encrypted_data)
            credit_write.close()
            print("updated")
        else:
            encrypted_data = f.encrypt(str({variable: value}).encode())
            credit_write = open(credential_path, "wb")
            credit_write.write(encrypted_data)
            credit_write.close()
            print("written")

    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return

def read_credential(key):
    # decrypt data
    credential_path = "credentials.txt"
    credential = open(credential_path, "rb").read()
    f = Fernet(generate_key(key))
    try:
        if credential:
            decrypted_data = f.decrypt(credential)
            credit_dictionary = ast.literal_eval(decrypted_data.decode())
            print("-----------------------------------------")
            for x in credit_dictionary:
                print(x + ": " + str(credit_dictionary[x]))
            print("-----------------------------------------")
            return True
        else:
            print("no data")
            return True
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return False


def delete_crendential(key, variable):
    # decrypt data
    credential_path = "credentials.txt"
    credential = open(credential_path, "rb").read()
    f = Fernet(generate_key(key))
    try:
        if credential:
            decrypted_data = f.decrypt(credential)
            credit_dictionary = ast.literal_eval(decrypted_data.decode())
            credit_dictionary.pop(variable)
        else:
            print("no data")
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return