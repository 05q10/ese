# Vigenere Cipher

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    j = 0
    for ch in text:
        if ch in alphabet:
            shift = alphabet.index(key[j % len(key)])
            result += alphabet[(alphabet.index(ch) + shift) % 26]
            j += 1
        else:
            result += ch
    return result

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    j = 0
    for ch in text:
        if ch in alphabet:
            shift = alphabet.index(key[j % len(key)])
            result += alphabet[(alphabet.index(ch) - shift) % 26]
            j += 1
        else:
            result += ch
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    key = input("Enter key: ")
    enc = vigenere_encrypt(msg, key)
    print("Encrypted:", enc)
    print("Decrypted:", vigenere_decrypt(enc, key))
