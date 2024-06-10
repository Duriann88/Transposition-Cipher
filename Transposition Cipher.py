def transposition_encrypt(text, key):
    encrypted_text = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            encrypted_text[col] += text[pointer]
            pointer += key
    return ''.join(encrypted_text)

def transposition_decrypt(text, key):
    num_of_columns = int(len(text) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)

    decrypted_text = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in text:
        decrypted_text[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(decrypted_text)


def main():
    print("Transposition Cipher Encryption and Decryption")

    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = int(input("Enter the key: "))
            ciphertext = transposition_encrypt(plaintext, key)
            print(f"Encrypted Text: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            key = int(input("Enter the key: "))
            plaintext = transposition_decrypt(ciphertext, key)
            print(f"Decrypted Text: {plaintext}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
