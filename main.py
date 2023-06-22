from encryptor import encrypt, decrypt, generate_key
from credential import add_credential, read_credential, delete_crendential
import os.path
import time
from colorama import init as colorama_init
from colorama import Fore, Back, Style
colorama_init()

def textc(color, text):
    return f"{color}{text}{Style.RESET_ALL}"


def banner():
    dos_rebel_style = [
        " ██████████                                                     █████",
        "░░███░░░░░█                                                    ░░███",
        " ░███  █ ░  ████████    ██████  ████████  █████ ████ ████████  ███████    ██████  ████████",
        " ░██████   ░░███░░███  ███░░███░░███░░███░░███ ░███ ░░███░░███░░░███░    ███░░███░░███░░███",
        " ░███░░█    ░███ ░███ ░███ ░░░  ░███ ░░░  ░███ ░███  ░███ ░███  ░███    ░███ ░███ ░███ ░░░",
        " ░███ ░   █ ░███ ░███ ░███  ███ ░███      ░███ ░███  ░███ ░███  ░███ ███░███ ░███ ░███",
        " ██████████ ████ █████░░██████  █████     ░░███████  ░███████   ░░█████ ░░██████  █████",
        "░░░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░       ░░░░░███  ░███░░░     ░░░░░   ░░░░░░  ░░░░░",
        "                                           ███ ░███  ░███",
        "                                          ░░██████   █████",
        "                                           ░░░░░░   ░░░░░",
    ]

    ansi_shadow = [
        "    ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗",
        "    ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗",
        "    █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝",
        "    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗",
        "    ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║",
        "    ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝",
    ]

    alligator_two = [
        ":::::::::: ::::    :::  ::::::::  :::::::::  :::   ::: ::::::::: ::::::::::: ::::::::  :::::::::  ",
        ":+:        :+:+:   :+: :+:    :+: :+:    :+: :+:   :+: :+:    :+:    :+:    :+:    :+: :+:    :+: ",
        "+:+        :+:+:+  +:+ +:+        +:+    +:+  +:+ +:+  +:+    +:+    +:+    +:+    +:+ +:+    +:+ ",
        "+#++:++#   +#+ +:+ +#+ +#+        +#++:++#:    +#++:   +#++:++#+     +#+    +#+    +:+ +#++:++#:  ",
        "+#+        +#+  +#+#+# +#+        +#+    +#+    +#+    +#+           +#+    +#+    +#+ +#+    +#+ ",
        "#+#        #+#   #+#+# #+#    #+# #+#    #+#    #+#    #+#           #+#    #+#    #+# #+#    #+# ",
        "########## ###    ####  ########  ###    ###    ###    ###           ###     ########  ###    ### ",
    ]

    my_name = [
        "   __            ______    __    _ __ __                    _ ",
        "  / /  __ __    /  _/ /__ / /__ (_) //_/__  __ _  ___  ____(_)",
        " / _ \/ // /   _/ //  '_//  '_// / ,< / _ \/  ' \/ _ \/ __/ / ",
        "/_.__/\_, /   /___/_/\_\/_/\_\/_/_/|_|\___/_/_/_/\___/_/ /_/  ",
        "     /___/                                                    ",
    ]

    for lines in dos_rebel_style:
        print(textc(Fore.LIGHTCYAN_EX, lines))
    for lines in my_name:
        print(textc(Fore.BLUE, lines))


def impossible_error():
    talking_head = [
        "        ██╗  ██╗ ██████╗ ██╗    ██╗    ██████╗ ██╗██████╗     ██╗         ",
        "        ██║  ██║██╔═══██╗██║    ██║    ██╔══██╗██║██╔══██╗    ██║         ",
        "        ███████║██║   ██║██║ █╗ ██║    ██║  ██║██║██║  ██║    ██║         ",
        "        ██╔══██║██║   ██║██║███╗██║    ██║  ██║██║██║  ██║    ██║         ",
        "        ██║  ██║╚██████╔╝╚███╔███╔╝    ██████╔╝██║██████╔╝    ██║         ",
        "        ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝     ╚═════╝ ╚═╝╚═════╝     ╚═╝         ",
        "                                                                          ",
        " ██████╗ ███████╗████████╗    ██╗  ██╗███████╗██████╗ ███████╗    ██████╗ ",
        "██╔════╝ ██╔════╝╚══██╔══╝    ██║  ██║██╔════╝██╔══██╗██╔════╝    ╚════██╗",
        "██║  ███╗█████╗     ██║       ███████║█████╗  ██████╔╝█████╗        ▄███╔╝",
        "██║   ██║██╔══╝     ██║       ██╔══██║██╔══╝  ██╔══██╗██╔══╝        ▀▀══╝ ",
        "╚██████╔╝███████╗   ██║       ██║  ██║███████╗██║  ██║███████╗      ██╗   ",
        " ╚═════╝ ╚══════╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝      ╚═╝   "
    ]

    for lines in talking_head:
        print(textc(Fore.LIGHTRED_EX, lines))

def choice(query, zero, one):
    """
    binary choice, return true and false
    """
    while True:
        input_data = input(textc(Fore.LIGHTWHITE_EX, query))
        if input_data == zero or input_data == one:
            if input_data == zero:
                return True
            elif input_data == "back":
                return "back"
            else:
                return False
        else:
            print(textc(Fore.YELLOW, "answer not match"))


def multichoice(query, *choices):
    """
    infinite choice length, return the choices
    """
    while True:
        input_data = input(textc(Fore.LIGHTWHITE_EX, query))
        for cho in choices:
            if cho == input_data:
                return input_data
        else:
            print(textc(Fore.YELLOW, "answer not match"))


def checkfile():
    while True:
        input_data = input(textc(Fore.LIGHTWHITE_EX, "Path(with extension): "))
        if os.path.isfile(input_data):
            return input_data
        else:
            print(textc(Fore.YELLOW, "File not found"))


def main():
    program_choice = choice("manage credentials or encrypt files(credit/encrypt): ", "credit", "encrypt")
    if program_choice:
        credential_program()
    else:
        encryption_program()

    halt = input(textc(Fore.LIGHTBLUE_EX, "Type 'r' to restart, press anything to exit... "))
    if halt == "r":
        main()

def credential_program():
    def write():
        print(textc(Fore.LIGHTWHITE_EX, "Which item you want to add/change?"))
        input_variable = input(textc(Fore.LIGHTWHITE_EX, "Input variable: "))
        input_value = input(textc(Fore.LIGHTWHITE_EX, "Input value: "))
        add_credential(password, input_variable, input_value)
        read_credential(password)
    def delete():
        input_variable = input(textc(Fore.LIGHTWHITE_EX, "what item you want to delete(type 'back' to go back): "))
        if input_variable == "back":
            credential_program()
        deleted = delete_crendential(password, input_variable)
        if deleted:
            delete()

    credit_choice = multichoice("see, add/change, or delete credentials(see/add/delete/back(go back)): ", "see", "add", "delete", "back")
    if credit_choice == "back":
        main()
    elif credit_choice == "see":
        password = input(textc(Fore.LIGHTWHITE_EX, "Input password: "))
        read_credential(password)
    elif credit_choice == "add":
        print(textc(Fore.YELLOW, "(If credentials is empty, input the new password here)"))
        password = input(textc(Fore.LIGHTWHITE_EX, "Input password: "))
        reading = read_credential(password)
        if reading:
            write()
    elif credit_choice == "delete":
        password = input(textc(Fore.LIGHTWHITE_EX, "Input password: "))
        reading = read_credential(password)
        if reading and reading != "no data":
            delete()
        read_credential(password)
    else:
        impossible_error()
    stop = input(textc(Fore.LIGHTBLUE_EX, "Type 'back' to restart program, otherwise press anything to exit program... "))
    if stop == "back":
        credential_program()
    else:
        print("wait...")
        time.sleep(2)

def encryption_program():
    crypt_choice = choice("encrypt or decrypt, type 'back' to go back: ", "encrypt", "decrypt")
    if crypt_choice == "back":
        main()
    elif crypt_choice:
        file = checkfile()
        password = input(textc(Fore.LIGHTWHITE_EX, "Input password: "))
        key = generate_key(password)
        encrypt(file, key)
    else:
        file = checkfile()
        password = input(textc(Fore.LIGHTWHITE_EX, "Input password: "))
        key = generate_key(password)
        decrypt(file, key)
    stop = input(textc(Fore.LIGHTBLUE_EX, "Type 'back' to restart program, otherwise press anything to exit program... "))
    if stop == "back":
        encryption_program()
    else:
        print("wait...")
        time.sleep(2)


if __name__ == "__main__":
    banner()
    print(textc(Fore.LIGHTBLUE_EX, "Welcome! this is an encryption program made by me(can't help the ascii header it's too good)"))
    main()

"""
coloring convention:
cyan: welcome text
lime: prompt
yellow: warning
red: error
"""


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
