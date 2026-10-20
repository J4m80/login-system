import hashlib
import hmac
import os

ITERATIONS = 100_000


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, ITERATIONS
    )
    return salt, password_hash


def verify_password(password, salt, stored_hash):
    _, new_hash = hash_password(password, salt)
    return hmac.compare_digest(new_hash, stored_hash)
