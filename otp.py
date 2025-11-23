# One-Time Pad

import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def otp_encrypt(text):
    text = text.upper()
    key = "".join(random.choice(alphabet) for _ in range(len(text)))
    result = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            result += alphabet[(alphabet.index(text[i]) + alphabet.index(key[i])) % 26]
        else:
            result += text[i]
    return result, key

def otp_decrypt(cipher, key):
    result = ""
    for i in range(len(cipher)):
        if cipher[i] in alphabet:
            result += alphabet[(alphabet.index(cipher[i]) - alphabet.index(key[i])) % 26]
        else:
            result += cipher[i]
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    cipher, key = otp_encrypt(msg)
    print("Encrypted:", cipher)
    print("Key:", key)
    print("Decrypted:", otp_decrypt(cipher, key))
