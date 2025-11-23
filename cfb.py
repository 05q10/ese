BLOCK_SIZE = 8

def xor_block(a, b):
    return "".join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def cfb_encrypt(text, key, iv):
    cipher = ""
    prev = iv

    for i in range(0, len(text), BLOCK_SIZE):
        block = text[i:i+BLOCK_SIZE].ljust(BLOCK_SIZE, "X")
        encrypted = xor_block(prev, key)   # Encrypt previous cipher
        cipher_block = xor_block(block, encrypted)
        cipher += cipher_block
        prev = cipher_block
    return cipher

def cfb_decrypt(cipher, key, iv):
    plain = ""
    prev = iv

    for i in range(0, len(cipher), BLOCK_SIZE):
        block = cipher[i:i+BLOCK_SIZE]
        encrypted = xor_block(prev, key)
        plain_block = xor_block(block, encrypted)
        plain += plain_block
        prev = block

    return plain.rstrip("X")

# test
if __name__ == "__main__":
    key = "ABCDEFGH"
    iv  = "HGFEDCBA"
    msg = input("Enter message: ")
    enc = cfb_encrypt(msg, key, iv)
    print("Encrypted:", enc)
    print("Decrypted:", cfb_decrypt(enc, key, iv))
