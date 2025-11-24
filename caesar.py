# Caesar Cipher (Shift = 3)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(text):
    shift = 3
    text = text.upper()
    result = ""
    for ch in text:
        if ch in alphabet:
            result += alphabet[(alphabet.index(ch) + shift) % 26]
        else:
            result += ch
    return result

def caesar_decrypt(text):
    shift = 3
    text = text.upper()
    result = ""
    for ch in text:
        if ch in alphabet:
            result += alphabet[(alphabet.index(ch) - shift) % 26]
        else:
            result += ch
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    enc = caesar_encrypt(msg)
    print("Encrypted:", enc)
    print("Decrypted:", caesar_decrypt(enc))