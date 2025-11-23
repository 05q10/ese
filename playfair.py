# Playfair Cipher

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    used = []
    for ch in key:
        if ch not in used and ch in alphabet:
            used.append(ch)
    for ch in alphabet:
        if ch not in used:
            used.append(ch)
    return [used[i:i+5] for i in range(0, 25, 5)]

def locate(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None

def prepare(text):
    text = text.upper().replace("J", "I")
    i = 0
    result = ""
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 == 1:
        result += "X"
    return result

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = locate(matrix, a)
        r2, c2 = locate(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

def playfair_decrypt(text, key):
    matrix = generate_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = locate(matrix, a)
        r2, c2 = locate(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

# Example
if __name__ == "__main__":
    msg = input("Enter message: ")
    key = input("Enter Playfair key: ")
    enc = playfair_encrypt(msg, key)
    print("Encrypted:", enc)
    print("Decrypted:", playfair_decrypt(enc, key))
