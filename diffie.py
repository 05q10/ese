# Diffie-Hellman Key Exchange (Simple Implementation)

def diffie_hellman(p, g, a, b):
    """
    p  = large prime (public)
    g  = primitive root modulo p (public)
    a  = Alice's private key
    b  = Bob's private key
    """

    # Step 1: Public values
    print(f"Public Prime (p): {p}")
    print(f"Primitive Root (g): {g}")

    # Step 2: Alice computes A = g^a mod p
    A = pow(g, a, p)
    print(f"\nAlice's Private Key (a): {a}")
    print(f"Alice sends A = g^a mod p = {A}")

    # Step 3: Bob computes B = g^b mod p
    B = pow(g, b, p)
    print(f"\nBob's Private Key (b): {b}")
    print(f"Bob sends B = g^b mod p = {B}")

    # Step 4: Shared Secret Calculation
    secret_A = pow(B, a, p)   # Alice computes
    secret_B = pow(A, b, p)   # Bob computes

    print("\nAlice computes shared secret = B^a mod p =", secret_A)
    print("Bob computes shared secret   = A^b mod p =", secret_B)

    return secret_A, secret_B


# MAIN PROGRAM
if __name__ == "__main__":
    print("---- Diffie-Hellman Key Exchange ----")
    
    # Use a safe prime and primitive root
    p = int(input("Enter a large prime number p: "))
    g = int(input("Enter primitive root g: "))

    a = int(input("Enter Alice's private key a: "))
    b = int(input("Enter Bob's private key b: "))

    secretA, secretB = diffie_hellman(p, g, a, b)

    print("\nShared Secret Key (Alice):", secretA)
    print("Shared Secret Key (Bob):  ", secretB)

    if secretA == secretB:
        print("\nKey Exchange Successful! Shared key established.")
    else:
        print("\nError: Keys do not match.")
