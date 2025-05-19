Encrypted Journal - Command Line Python Project
------------------------------------------------

This is a simple command-line journal where your notes are securely encrypted using a password. Only someone with the correct password can view the entries.

How It Works:
-------------
- You write a journal entry.
- The entry is encrypted and saved to a file.
- You can later decrypt and read your entries using the same password.

What You Need:
--------------
- Python 3
- cryptography library

To install cryptography:
-------------------------
Open your terminal or command prompt and run:

    pip install cryptography

How To Use:
-----------
1. Save the script as: encrypted_journal.py
2. Open your terminal in the same folder.
3. Run the script:

    python encrypted_journal.py

4. It will ask you to choose:
    - 1 to write a new entry
    - 2 to read entries

5. Then it will ask for your password.
6. Entries are saved to or read from a file named `journal.txt`.

Notes:
------
- The password is never saved.
- Without the correct password, you can't read the journal.
- Do not lose your password.

File Structure:
---------------
- encrypted_journal.py  → the Python script
- journal.txt           → your encrypted data file (auto-created)

