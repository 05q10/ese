BLOCK_SIZE = 8

def pad(text):
    while len(text) % BLOCK_SIZE != 0:
        text += "X"
    return text

def xor_block(block, key):
    return "".join(chr(ord(block[i]) ^ ord(key[i])) for i in range(BLOCK_SIZE))

def ecb_encrypt(text, key):
    text = pad(text)
    cipher = ""
    for i in range(0, len(text), BLOCK_SIZE):
        block = text[i:i+BLOCK_SIZE]
        cipher += xor_block(block, key)
    return cipher

def ecb_decrypt(cipher, key):
    plain = ""
    for i in range(0, len(cipher), BLOCK_SIZE):
        block = cipher[i:i+BLOCK_SIZE]
        plain += xor_block(block, key)
    return plain.rstrip("X")

# test
if __name__ == "__main__":
    key = "ABCDEFGH"
    msg = input("Enter message: ")
    enc = ecb_encrypt(msg, key)
    print("Encrypted:", enc)
    print("Decrypted:", ecb_decrypt(enc, key))
