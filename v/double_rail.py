# ---------------------------------------
# Rail Fence Cipher — Single Encryption
# ---------------------------------------
def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "").upper()
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    row, down = 0, True

    for col, ch in enumerate(text):
        fence[row][col] = ch

        if row == rails - 1:
            down = False
        elif row == 0:
            down = True

        row += 1 if down else -1

    # Join all rows
    result = "".join("".join(r) for r in fence)
    return result


# ---------------------------------------
# Rail Fence Cipher — Single Decryption
# ---------------------------------------
def rail_fence_decrypt(cipher, rails):
    cipher = cipher.replace(" ", "").upper()
    fence = [['' for _ in range(len(cipher))] for _ in range(rails)]
    row, down = 0, True

    # Mark zig-zag pattern
    for col in range(len(cipher)):
        fence[row][col] = '*'
        if row == rails - 1:
            down = False
        elif row == 0:
            down = True
        row += 1 if down else -1

    print("\nZigzag structure for rails =", rails)
    for r in fence: print(r)

    # Fill ciphertext row-wise
    idx = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == '*':
                fence[r][c] = cipher[idx]
                idx += 1

    print("\nFilled fence:")
    for r in fence: print(r)

    # Read zig-zag to get plaintext
    result = ""
    row, down = 0, True
    for col in range(len(cipher)):
        result += fence[row][col]
        if row == rails - 1:
            down = False
        elif row == 0:
            down = True
        row += 1 if down else -1

    return result


# ---------------------------------------
# Double Rail Fence Cipher Encryption
# ---------------------------------------
def double_rail_fence_encrypt(text, rails1, rails2):

    print("\n---- DOUBLE RAIL FENCE ENCRYPTION ----")
    print("\nOriginal Text:", text)

    # First encryption
    enc1 = rail_fence_encrypt(text, rails1)
    print("\nAfter 1st Rail Fence (rails =", rails1, "):", enc1)

    # Second encryption
    enc2 = rail_fence_encrypt(enc1, rails2)
    print("\nAfter 2nd Rail Fence (rails =", rails2, "):", enc2)

    return enc2


# ---------------------------------------
# Double Rail Fence Cipher Decryption
# ---------------------------------------
def double_rail_fence_decrypt(cipher, rails1, rails2):

    print("\n---- DOUBLE RAIL FENCE DECRYPTION ----")
    print("\nFinal Cipher Received:", cipher)

    # First decrypt with second key
    dec1 = rail_fence_decrypt(cipher, rails2)
    print("\nAfter 1st Decryption (rails =", rails2, "):", dec1)

    # Then decrypt with first key
    dec2 = rail_fence_decrypt(dec1, rails1)
    print("\nAfter 2nd Decryption (rails =", rails1, "):", dec2)

    return dec2


# ---------------------------------------
# Example Execution
# ---------------------------------------
if __name__ == "__main__":
    msg = input("Enter message: ")
    rails1 = int(input("Enter rails for first encryption: "))
    rails2 = int(input("Enter rails for second encryption: "))

    encrypted = double_rail_fence_encrypt(msg, rails1, rails2)
    print("\nDouble Encrypted Text:", encrypted)

    decrypted = double_rail_fence_decrypt(encrypted, rails1, rails2)
    print("\nFinal Decrypted Text:", decrypted)
