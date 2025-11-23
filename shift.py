# Shift Cipher (User-defined shift)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift_encrypt(text, shift):
    text = text.upper()
    result = ""
    for ch in text:
        if ch in alphabet:
            result += alphabet[(alphabet.index(ch) + shift) % 26]
        else:
            result += ch
    return result

def shift_decrypt(text, shift):
    return shift_encrypt(text, -shift)

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    shift = int(input("Enter shift value: "))
    enc = shift_encrypt(msg, shift)
    print("Encrypted:", enc)
    print("Decrypted:", shift_decrypt(enc, shift))
