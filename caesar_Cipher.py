def encrypt(text, shift):
    """
    Encrypts the given text using Caesar Cipher with the specified shift
    """
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, shift):
    """
    Decrypts the given text using Caesar Cipher with the specified shift.
    """
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    while True:
        choice = input("Choose (E)ncrypt, (D)ecrypt or (Q)uit: ").strip().upper()
        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        if choice not in ('E', 'D'):
            print("Invalid choice. Please choose again.")
            continue
        
        message = input("Enter your message: ")
        while True:
            try:
                shift = int(input("Enter shift value (integer): "))
                break
            except ValueError:
                print("Invalid number. Please enter an integer.")

        if choice == 'E':
            encrypted = encrypt(message, shift)
            print(f"Encrypted message: {encrypted}")
        else:
            decrypted = decrypt(message, shift)
            print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
