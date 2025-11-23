# Double Transposition Cipher

from columnar import columnar_encrypt, columnar_decrypt

def double_encrypt(text, key1, key2):
    step1 = columnar_encrypt(text, key1)
    step2 = columnar_encrypt(step1, key2)
    return step2

def double_decrypt(cipher, key1, key2):
    step1 = columnar_decrypt(cipher, key2)
    step2 = columnar_decrypt(step1, key1)
    return step2

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    key1 = input("Enter first key: ").upper()
    key2 = input("Enter second key: ").upper()

    enc = double_encrypt(msg, key1, key2)
    print("Encrypted:", enc)
    print("Decrypted:", double_decrypt(enc, key1, key2))
