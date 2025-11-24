def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift = key % 26
            if char.isupper():
                # Convert A-Z (65-90)
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                # Convert a-z (97-122)
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep spaces, punctuation
        
    return result


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char

    return result


def main():
    # Take input from user
    text = input("Enter text: ")
    key = int(input("Enter key (number): "))

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("\n--- RESULTS ---")
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)


# Run the program
if __name__ == "__main__":
    main()
