# -------------------------------
#  RSA + CAESAR HYBRID CRYPTO
# -------------------------------

import random

# ------------------ CAESAR CIPHER ------------------

def caesar_encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result


def caesar_decrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch
    return result


# ------------------ PURE RSA ------------------

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    # Extended Euclid (iterative)
    t1, t2 = 0, 1
    r1, r2 = phi, e

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        r1, r2 = r2, r
        t1, t2 = t2, t

    if r1 != 1:
        return None

    return t1 % phi


def generate_prime():
    primes = [101, 103, 107, 109, 113, 127]
    return random.choice(primes)


def rsa_generate_keypair():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  # small public exponent
    d = mod_inverse(e, phi)

    if d is None:
        return rsa_generate_keypair()

    return (e, n), (d, n)


def rsa_encrypt(num, public_key):
    e, n = public_key
    return pow(num, e, n)


def rsa_decrypt(num, private_key):
    d, n = private_key
    return pow(num, d, n)


# ------------------ HYBRID FUNCTIONS ------------------

def hybrid_encrypt(plaintext, rsa_public_key):
    # 1. Generate Caesar key K
    K = random.randint(1, 25)
    print("\n[+] Random Caesar key generated:", K)

    # 2. Caesar encrypt message
    encrypted_msg = caesar_encrypt(plaintext, K)

    # 3. Encrypt K using RSA
    encrypted_key = rsa_encrypt(K, rsa_public_key)

    # return both encrypted parts
    return encrypted_msg, encrypted_key


def hybrid_decrypt(encrypted_msg, encrypted_key, rsa_private_key):
    # 1. Recover Caesar key
    K = rsa_decrypt(encrypted_key, rsa_private_key)
    print("\n[+] Caesar key recovered:", K)

    # 2. Caesar decrypt message
    decrypted_msg = caesar_decrypt(encrypted_msg, K)

    return decrypted_msg


# ------------------ DEMO ------------------

def main():
    # Step 1 — RSA key generation
    public_key, private_key = rsa_generate_keypair()
    print("PUBLIC KEY:", public_key)
    print("PRIVATE KEY:", private_key)

    # Step 2 — Plain message
    message = "HELLO ALICE THIS IS A SECRET MESSAGE!"
    print("\nOriginal text:", message)

    # Step 3 — Hybrid encryption
    encrypted_msg, encrypted_key = hybrid_encrypt(message, public_key)

    print("\nEncrypted Caesar message:", encrypted_msg)
    print("Encrypted Caesar key (RSA):", encrypted_key)

    # Step 4 — Hybrid decryption
    decrypted_msg = hybrid_decrypt(encrypted_msg, encrypted_key, private_key)

    print("\nDecrypted text:", decrypted_msg)


if __name__ == "__main__":
    main()
