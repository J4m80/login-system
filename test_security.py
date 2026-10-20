from security import hash_password, verify_password


def test_correct_password_is_accepted():
    salt, stored_hash = hash_password("secret123")
    assert verify_password("secret123", salt, stored_hash) is True

def test_incorrect_password():
    salt, stored_hash = hash_password("secret123")
    assert verify_password("seCret123", salt, stored_hash) is False

def test_random_salt():
    salt1, _ = hash_password("secret123")
    salt2, _ = hash_password("secret123")
    assert salt1 != salt2

def test_same_salt_gives_same_hash():
    salt, _ = hash_password("secret123")
    _, hash1 = hash_password("secret123", salt)
    _, hash2 = hash_password("secret123", salt)
    assert hash1 == hash2
