#!/usr/bin/python3
"""
MIMI Crypto
Author: fourdim
Github: fourdim/mimi
Version: 0.1.0
Tip:
The output of the program in different versions may not be the same.
"""

import base64
import hashlib

def mi_decode(text, password):
    """Decode."""
    text = text.decode()
    length = len(text)
    password = str(length) + password
    password_lenth = len(password) + 1
    password = long_password(length, password)
    password = password[password_lenth::2]
    new_text = ""
    for i in range(length):
        new_text = new_text+ chr(ord(text[i]) - ord(password[i]))
    new_text = base64.b64decode(new_text)
    return new_text

def mi_encode(text, password):
    """Encode."""
    text = base64.b64encode(text)
    text = text.decode()
    length = len(text)
    password = str(length) + password
    password_lenth = len(password) + 1
    password = long_password(length, password)
    password = password[password_lenth::2]
    new_text = ""
    for i in range(length):
        new_text = new_text+ chr(ord(text[i]) + ord(password[i]))
    new_text = new_text.encode()
    return new_text

def long_password(length, password):
    """Extend the password."""
    count = 0
    while count < (length//32 + 3):
        password = password + hashlib.sha256(password.encode()).hexdigest()
        count = count + 1
    return password

def main():
    """Main function."""
    file_path = input("Filepath > ")
    file_path = file_path.replace('"', '')
    password = input("password > ").encode()
    hash_value = hashlib.sha256(password).hexdigest()
    with open(file_path, "rb") as file1:
        text = file1.read()
    if file_path.endswith(".mi"):
        new_text = mi_decode(text, hash_value)
    else:
        new_text = mi_encode(text, hash_value)
    if file_path.endswith(".mi"):
        folder = file_path.rfind(".mi")
        file_path = file_path[0:folder]
        with open(file_path, "wb") as file2:
            file2.write(new_text)
    else:
        file_path = file_path + ".mi"
        with open(file_path, "wb") as file2:
            file2.write(new_text)

if __name__ == "__main__":
    main()
