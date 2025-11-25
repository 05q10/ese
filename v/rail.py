# Rail Fence Cipher

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
    # print(fence)

    result = "".join("".join(row) for row in fence)
    return result

def rail_fence_decrypt(cipher, rails):
    cipher = cipher.replace(" ", "").upper()
    fence = [['' for _ in range(len(cipher))] for _ in range(rails)]
    row, down = 0, True

    # mark zigzag structure
    for col in range(len(cipher)):
        fence[row][col] = '*'
        if row == rails - 1:
            down = False
        elif row == 0:
            down = True
        row += 1 if down else -1

    print(fence)

    # fill cipher text
    idx = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == '*':
                fence[r][c] = cipher[idx]
                idx += 1
    print()
    print(fence)

    # read zigzag
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

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    rails = int(input("Enter number of rails: "))
    enc = rail_fence_encrypt(msg, rails)
    print("Encrypted:", enc)
    print("Decrypted:", rail_fence_decrypt(enc, rails))
