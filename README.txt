SECURE PASSWORD MANAGER (PYTHON)

A secure, offline-first password manager built using Python, designed with strong
cryptographic principles and a clean modular architecture.

This project demonstrates real-world cybersecurity practices including
password hashing, encryption, and secure local storage.


FEATURES
--------
• Master password authentication using PBKDF2 + salt
• AES-256 encryption for stored credentials
• Secure SQLite-based local vault
• Add, view, and manage passwords
• Strong password generator
• Modular and extensible architecture
• Command-line interface (CLI)
• Fully offline (no cloud dependency)


SYSTEM ARCHITECTURE
-------------------
User
 |
 v
CLI Interface (main.py)
 |
 v
Authentication Layer (auth.py)
 |  - PBKDF2-HMAC-SHA256
 |
 v
Encryption Engine (crypto.py)
 |  - AES-256 (Fernet)
 |
 v
Secure Vault (SQLite Database)
    - Encrypted usernames
    - Encrypted passwords


SECURITY DESIGN
---------------
Master Password Protection
• Master password is never stored
• Hashed using PBKDF2-HMAC-SHA256
• Random salt with high iteration count

Data Encryption
• AES-256 encryption (Fernet)
• Each credential encrypted individually
• Encryption key derived from master password

Secure Storage
• SQLite database
• No plaintext credentials stored
• Database locked during runtime


PROJECT STRUCTURE
-----------------
password-manager/
|
|-- main.py        : Application entry point (CLI)
|-- auth.py        : Password hashing and verification
|-- crypto.py      : Encryption and key derivation
|-- database.py   : Database initialization
|-- vault.py       : Secure CRUD operations
|-- generator.py  : Strong password generator
|-- requirements.txt
|-- README.txt
|-- vault.db       : Encrypted vault (auto-created, gitignored)


INSTALLATION & SETUP
--------------------
1. Clone the repository
   git clone https://github.com/manaskhanger/password-manager.git
   cd password-manager

2. Create and activate virtual environment
   python -m venv .venv
   .venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt


RUNNING THE APPLICATION
-----------------------
python main.py


FIRST RUN FLOW
--------------
=== First Time Setup ===
Create Master Password:
Confirm Master Password:

• Master password is created
• Hash and salt are stored securely
• Encryption key is derived


NORMAL RUN FLOW
---------------
Enter Master Password:
Authentication successful.


FUNCTIONAL FLOW
---------------
Start
 |
 |-- First Run?
 |     |-- Yes -> Create Master Password
 |     |-- No  -> Authenticate User
 |
 |-- Derive Encryption Key
 |
 |-- Display Menu
 |     |-- Add Password
 |     |-- View Passwords
 |     |-- Generate Password
 |     |-- Exit
 |
 '-- Close Database Securely


EXAMPLE USAGE
-------------
Add Password
Service: gmail
Username: user@gmail.com
Password: ********

View Passwords
Service: gmail
Username: user@gmail.com
Password: ********


FUTURE ENHANCEMENTS
-------------------
• GUI version (Tkinter / PyQt)
• Web application (FastAPI + React)
• Auto-lock after inactivity
• Clipboard copy with auto-clear
• Two-Factor Authentication (TOTP)
• Encrypted cloud sync
• Password breach detection


LEARNING OUTCOMES
-----------------
• Cryptography fundamentals (hashing vs encryption)
• Secure key derivation techniques
• SQLite file locking and lifecycle management
• Modular Python application design
• Cybersecurity best practices


DISCLAIMER
----------
This project is intended for educational purposes only.
Do not use modified versions in production without a full security audit.


WHY THIS PROJECT STANDS OUT
---------------------------
• Uses real encryption (AES-256), not encoding
• Security-first architecture
• Clean separation of concerns
• Internship and placement ready
• Easily extendable into GUI or web applications


LICENSE
-------
MIT License
