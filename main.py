from encryptor import encrypt, decrypt, generate_key
from credential import add_credential, read_credential
import os.path
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def choice(query, zero, one):
    while True:
        input_data = input(query)
        if input_data == zero or input_data == one:
            if input_data == zero:
                return True
            else:
                return False
        else:
            print("answer not match")


def checkfile():
    while True:
        input_data = input("Path(with extension): ")
        if os.path.isfile(input_data):
            return input_data
        else:
            print("file not found")


def main():
    print("welcome, this is an encryption program made by me")
    program_choice = choice("see credentials or encrypt files(credit/encrypt): ", "credit", "encrypt")
    if program_choice:
        credential_program()
    else:
        encryption_program()

    halt = input("Type 'r' to restart, press anything to exit... ")
    if halt == "r":
        main()

def credential_program():
    def read():
        print("Which item you want to change/add?")
        input_variable = input("Input variable: ")
        input_value = input("Input value: ")
        add_credential(password, input_variable, input_value)
    credit_choice = choice("see credentials or add credentials(see/add): ", "see", "add")
    if credit_choice:
        password = input("Input password: ")
        reading = read_credential(password)
    else:
        password = input("Input password: ")
        reading = read_credential(password)
        if reading:
            read()
    stop = input("Type 'back' to restart program, otherwise press anything to exit program... ")
    if stop == "back":
        credential_program()

def encryption_program():
    crypt_choice = choice("encrypt or decrypt: ", "encrypt", "decrypt")
    if crypt_choice:
        file = checkfile()
        password = input("Input password: ")
        key = generate_key(password)
        encrypt(file, key)
    else:
        file = checkfile()
        password = input("Input password: ")
        key = generate_key(password)
        decrypt(file, key)
    stop = input("Type 'back' to restart program, otherwise press anything to exit program... ")
    if stop == "back":
        encryption_program()

if __name__ == "__main__":
    # main()
    print(Fore.GREEN + "helo")
    # print(f"This is {Fore.GREEN}color{Style.RESET_ALL}!")

# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser(description="File Encryptor Script with a Password")
#     parser.add_argument("file", help="File to encrypt/decrypt")
#     parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",
#                         type=int)
#     parser.add_argument("-e", "--encrypt", action="store_true",
#                         help="Whether to encrypt the file, only -e or -d can be specified.")
#     parser.add_argument("-d", "--decrypt", action="store_true",
#                         help="Whether to decrypt the file, only -e or -d can be specified.")
#
#     args = parser.parse_args()
#     file = args.file
#
#     if args.encrypt:
#         password = getpass.getpass("Enter the password for encryption: ")
#     elif args.decrypt:
#         password = getpass.getpass("Enter the password you used for encryption: ")
#
#     if args.salt_size:
#         key = generate_key(password, salt_size=args.salt_size, save_salt=True)
#     else:
#         key = generate_key(password, load_existing_salt=True)
#
#     encrypt_ = args.encrypt
#     decrypt_ = args.decrypt
#
#     if encrypt_ and decrypt_:
#         raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
#     elif encrypt_:
#         encrypt(file, key)
#     elif decrypt_:
#         decrypt(file, key)
#     else:
#         raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")

# def generate_salt(size=16):
#     """Generate the salt used for key derivation,
#     `size` is the length of the salt to generate"""
#     return secrets.token_bytes(size)


# def load_salt():
#     # load salt from salt.salt file
#     return open("salt.salt", "rb").read()
