BLOCK_SIZE = 8

def pad(text):
    while len(text) % BLOCK_SIZE != 0:
        text += "X"
    return text

def xor_block(block, key):
    return "".join(chr(ord(block[i]) ^ ord(key[i])) for i in range(BLOCK_SIZE))

def cbc_encrypt(text, key, iv):
    text = pad(text)
    cipher = ""
    prev = iv

    for i in range(0, len(text), BLOCK_SIZE):
        block = text[i:i+BLOCK_SIZE]
        mixed = xor_block(block, prev)     # XOR plaintext with previous cipher
        encrypted = xor_block(mixed, key)  # Encrypt
        cipher += encrypted
        prev = encrypted
    return cipher

def cbc_decrypt(cipher, key, iv):
    plain = ""
    prev = iv

    for i in range(0, len(cipher), BLOCK_SIZE):
        block = cipher[i:i+BLOCK_SIZE]
        mixed = xor_block(block, key)       # Decrypt
        plain += xor_block(mixed, prev)     # XOR with previous ciphertext
        prev = block

    return plain.rstrip("X")

# test
if __name__ == "__main__":
    key = "ABCDEFGH"
    iv  = "HGFEDCBA"
    msg = input("Enter message: ")
    enc = cbc_encrypt(msg, key, iv)
    print("Encrypted:", enc)
    print("Decrypted:", cbc_decrypt(enc, key, iv))
