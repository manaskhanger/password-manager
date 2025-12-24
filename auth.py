import hashlib, os

def hash_password(password, salt=None):
    if not salt:
        salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200000)
    return salt, pwd_hash

def verify_password(password, salt, stored_hash):
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200000)
    return new_hash == stored_hash
