BLOCK_SIZE = 8

def xor_block(a, b):
    return "".join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def int_to_block(counter):
    return str(counter).zfill(8)  # convert number → 8 chars

def ctr_encrypt(text, key, counter):
    cipher = ""

    for i in range(0, len(text), BLOCK_SIZE):
        block = text[i:i+BLOCK_SIZE].ljust(BLOCK_SIZE, "X")
        counter_block = int_to_block(counter)
        keystream = xor_block(counter_block, key)
        cipher_block = xor_block(block, keystream)
        cipher += cipher_block
        counter += 1
    return cipher

ctr_decrypt = ctr_encrypt  # symmetric

# test
if __name__ == "__main__":
    key = "ABCDEFGH"
    counter = 1
    msg = input("Enter message: ")
    enc = ctr_encrypt(msg, key, counter)
    print("Encrypted:", enc)
    print("Decrypted:", ctr_decrypt(enc, key, counter))
