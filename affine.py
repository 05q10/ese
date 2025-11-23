# Affine Cipher

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    text = text.upper()
    result = ""
    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            result += alphabet[(a * idx + b) % 26]
        else:
            result += ch
    return result

def affine_decrypt(text, a, b):
    text = text.upper()
    result = ""
    inv_a = mod_inverse(a, 26)
    if inv_a is None:
        return "Invalid key: 'a' must be coprime with 26"
    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            result += alphabet[(inv_a * (idx - b)) % 26]
        else:
            result += ch
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    a = int(input("Enter key a: "))
    b = int(input("Enter key b: "))
    enc = affine_encrypt(msg, a, b)
    print("Encrypted:", enc)
    print("Decrypted:", affine_decrypt(enc, a, b))
