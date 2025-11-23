# Monoalphabetic Substitution Cipher

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mono_encrypt(text, key_map):
    text = text.upper()
    result = ""
    for ch in text:
        if ch in alphabet:
            result += key_map[alphabet.index(ch)]
        else:
            result += ch
    return result

def mono_decrypt(text, key_map):
    text = text.upper()
    inverse = {key_map[i]: alphabet[i] for i in range(26)}
    result = ""
    for ch in text:
        if ch in inverse:
            result += inverse[ch]
        else:
            result += ch
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    key_map = input("Enter 26-letter substitution key: ").upper()
    enc = mono_encrypt(msg, key_map)
    print("Encrypted:", enc)
    print("Decrypted:", mono_decrypt(enc, key_map))
