# Hill Cipher (2x2)

import numpy as np
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        vec = np.array([[alphabet.index(text[i])], [alphabet.index(text[i+1])]])
        res = np.dot(key, vec) % 26
        result += alphabet[res[0][0]] + alphabet[res[1][0]]
    return result

def hill_decrypt(text, key):
    det = int(round(np.linalg.det(key))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return "Invalid key matrix"

    adj = np.round(det * np.linalg.inv(key)).astype(int) % 26
    inv_key = (det_inv * adj) % 26

    result = ""
    for i in range(0, len(text), 2):
        vec = np.array([[alphabet.index(text[i])], [alphabet.index(text[i+1])]])
        res = np.dot(inv_key, vec) % 26
        result += alphabet[res[0][0]] + alphabet[res[1][0]]
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    print("Enter 2x2 matrix:")
    key = np.array([
        [int(input("a11: ")), int(input("a12: "))],
        [int(input("a21: ")), int(input("a22: "))]
    ])
    enc = hill_encrypt(msg, key)
    print("Encrypted:", enc)
    print("Decrypted:", hill_decrypt(enc, key))
