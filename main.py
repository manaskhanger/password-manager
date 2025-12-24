import sqlite3
import getpass
import sys
from auth import hash_password, verify_password
from crypto import derive_key
from database import init_db
from vault import add_entry, fetch_entries
from generator import generate_password

DB_NAME = "vault.db"


def setup_master_password(cursor, conn):
    print("\n=== First Time Setup ===")
    while True:
        master = getpass.getpass("Create Master Password: ")
        confirm = getpass.getpass("Confirm Master Password: ")

        if master != confirm:
            print("❌ Passwords do not match. Try again.")
        elif len(master) < 8:
            print("❌ Password must be at least 8 characters.")
        else:
            break

    salt, pwd_hash = hash_password(master)
    cursor.execute("INSERT INTO users VALUES (?, ?)", (salt, pwd_hash))
    conn.commit()
    print("✅ Master password created successfully.")
    return master, salt


def authenticate_user(cursor):
    cursor.execute("SELECT salt, password_hash FROM users")
    row = cursor.fetchone()

    if not row:
        return None, None

    salt, stored_hash = row
    attempts = 3

    while attempts > 0:
        master = getpass.getpass("Enter Master Password: ")
        if verify_password(master, salt, stored_hash):
            print("✅ Authentication successful.")
            return master, salt
        else:
            attempts -= 1
            print(f"❌ Incorrect password. Attempts left: {attempts}")

    print("🚫 Too many failed attempts. Exiting.")
    sys.exit(1)


def menu():
    print("\n==== PASSWORD MANAGER ====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Generate Strong Password")
    print("4. Exit")


def main():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    user_exists = cursor.fetchone()

    if not user_exists:
        master, salt = setup_master_password(cursor, conn)
    else:
        master, salt = authenticate_user(cursor)

    key = derive_key(master, salt)

    while True:
        menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            service = input("Service Name: ").strip()
            username = input("Username/Email: ").strip()
            password = getpass.getpass("Password: ").strip()

            if not service or not username or not password:
                print("❌ All fields are required.")
                continue

            add_entry(conn, key, service, username, password)
            print("✅ Password stored securely.")

        elif choice == "2":
            entries = fetch_entries(conn, key)
            if not entries:
                print("ℹ️ No saved passwords.")
            else:
                for idx, (service, username, password) in enumerate(entries, start=1):
                    print(f"\n{idx}. {service}")
                    print(f"   Username: {username}")
                    print(f"   Password: {password}")

        elif choice == "3":
            length = input("Password length (default 16): ").strip()
            length = int(length) if length.isdigit() else 16
            print("🔐 Generated Password:", generate_password(length))

        elif choice == "4":
            print("👋 Exiting.")
            conn.close()
            sys.exit(0)

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
