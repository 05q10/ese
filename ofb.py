BLOCK_SIZE = 8

def xor_block(a, b):
    return "".join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def ofb_encrypt(text, key, iv):
    cipher = ""
    feedback = iv

    for i in range(0, len(text), BLOCK_SIZE):
        block = text[i:i+BLOCK_SIZE].ljust(BLOCK_SIZE, "X")
        feedback = xor_block(feedback, key)   # Mode creates keystream
        cipher_block = xor_block(block, feedback)
        cipher += cipher_block
    return cipher

def ofb_decrypt(cipher, key, iv):
    return ofb_encrypt(cipher, key, iv)  # symmetric

# test
if __name__ == "__main__":
    key = "ABCDEFGH"
    iv  = "HGFEDCBA"
    msg = input("Enter message: ")
    enc = ofb_encrypt(msg, key, iv)
    print("Encrypted:", enc)
    print("Decrypted:", ofb_decrypt(enc, key, iv))
