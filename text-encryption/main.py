from cryptography.fernet import Fernet

# Generate key (only once)
key = Fernet.generate_key()
cipher = Fernet(key)

print(" Welcome to Text Encryption Tool")

while True:
    print("\n1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text to encrypt: ")
        encrypted = cipher.encrypt(text.encode())
        print(" Encrypted Text:")
        print(encrypted.decode())

    elif choice == "2":
        text = input("Enter encrypted text: ")
        try:
            decrypted = cipher.decrypt(text.encode())
            print(" Decrypted Text:")
            print(decrypted.decode())
        except:
            print("Invalid encrypted text")

    elif choice == "3":
        print(" Exiting...")
        break

    else:
        print("Invalid choice")
