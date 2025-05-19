from cryptography.fernet import Fernet
import hashlib
import os
import base64

# File where encrypted journal entries are stored
JOURNAL_FILE = "encrypted_journal.txt"

# Converts a plain password into a 32-byte key using SHA-256 hash
def generate_key(password: str) -> bytes:
    return hashlib.sha256(password.encode()).digest()

# Initializes a Fernet object using the hashed password
def get_fernet(password: str) -> Fernet:
    key = generate_key(password)
    # Fernet requires a base64-encoded 32-byte key
    return Fernet(base64.urlsafe_b64encode(key))

# Encrypts a journal message using the password
def encrypt_message(password: str, message: str) -> bytes:
    # Hash the password into a key
    key = generate_key(password)
    # Create a Fernet cipher with the key
    fernet = Fernet(base64.urlsafe_b64encode(key))
    # Encrypt the message and return the encrypted bytes
    return fernet.encrypt(message.encode())

# Decrypts an encrypted journal message using the password
def decrypt_message(password: str, token: bytes) -> str:
    # Hash the password into a key
    key = generate_key(password)
    # Create a Fernet cipher with the key
    fernet = Fernet(base64.urlsafe_b64encode(key))
    # Decrypt the token and convert it back to string
    return fernet.decrypt(token).decode()

# Adds a new encrypted entry to the journal file
def add_entry(password: str):
    entry = input("Write your journal entry:\n> ")
    # Encrypt the message
    encrypted = encrypt_message(password, entry)
    # Append the encrypted message to the file
    with open(JOURNAL_FILE, "ab") as file:
        file.write(encrypted + b"\n")
    print("✅ Entry saved and encrypted.")

# Reads and decrypts all entries from the journal file
def view_entries(password: str):
    if not os.path.exists(JOURNAL_FILE):
        print("📭 No journal found yet.")
        return

    with open(JOURNAL_FILE, "rb") as file:
        lines = file.readlines()

    print("\n🔓 Decrypted Journal Entries:\n" + "-" * 30)
    for i, line in enumerate(lines, 1):
        try:
            # Attempt to decrypt each line
            decrypted = decrypt_message(password, line.strip())
            print(f"{i}. {decrypted}")
        except Exception:
            # If decryption fails, likely due to wrong password
            print(f"{i}. 🔒 Unable to decrypt entry (wrong password?)")

# Main menu loop
def main():
    print("🔐 Welcome to Encrypted Journal CLI")
    password = input("Enter your journal password: ")

    # Loop until the user chooses to exit
    while True:
        print("\nOptions:\n1. Add Entry\n2. View Entries\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_entry(password)
        elif choice == "2":
            view_entries(password)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# Entry point for the program
if __name__ == "__main__":
    main()
