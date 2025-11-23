# Columnar Transposition Cipher (FULLY FIXED VERSION)

def create_order(key):
    return sorted(range(len(key)), key=lambda k: key[k])


def columnar_encrypt(text, key):
    text = text.replace(" ", "").upper()
    k = len(key)

    # Number of rows required
    rows = (len(text) + k - 1) // k
    matrix = []
    index = 0

    # Fill matrix row-wise, pad with X
    for r in range(rows):
        row = []
        for c in range(k):
            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append('X')
        matrix.append(row)

    order = create_order(key)
    cipher = ""

    # Read columns in sorted key order
    for col in order:
        for r in range(rows):
            cipher += matrix[r][col]

    return cipher


def columnar_decrypt(cipher, key):
    cipher = cipher.replace(" ", "").upper()
    k = len(key)
    n = len(cipher)

    rows = (n + k - 1) // k
    order = create_order(key)

    # Find which columns have fewer characters
    full_cols = n % k
    col_lengths = [rows] * k

    if full_cols != 0:
        for i in range(k):
            if order[i] >= full_cols:
                col_lengths[order[i]] -= 1

    # Create empty matrix
    matrix = [['' for _ in range(k)] for _ in range(rows)]
    idx = 0

    # Fill matrix column by column, respecting column lengths
    for col in order:
        length = col_lengths[col]
        for r in range(length):
            matrix[r][col] = cipher[idx]
            idx += 1

    result = ""
    # Read row-wise
    for r in range(rows):
        for c in range(k):
            if matrix[r][c] != '':
                result += matrix[r][c]

    return result.rstrip('X')  # Remove padding


# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    key = input("Enter key: ").upper()
    enc = columnar_encrypt(msg, key)
    print("Encrypted:", enc)
    print("Decrypted:", columnar_decrypt(enc, key))
