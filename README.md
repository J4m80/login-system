# Login System

![Tests](https://github.com/J4m80/login-system/actions/workflows/tests.yml/badge.svg)

A command-line authentication system in Python: registration, login, SQLite storage and secure password hashing.

## Features
- User registration and login via a text menu
- Passwords are never stored in plain text: hashed with PBKDF2-HMAC-SHA256 and a unique random 16-byte salt per user
- All SQL queries are parameterized, so the code is not vulnerable to SQL injection
- Hash comparison with `hmac.compare_digest`
- Generic error message on failed login, so attackers cannot find out which usernames exist
- Password input is hidden (`getpass`)
- Empty login or password is rejected, duplicate logins are handled

## Project structure
- `main.py` – menu and entry point
- `reg.py` – registration
- `log.py` – login
- `security.py` – password hashing and verification
- `test_security.py` – pytest tests for `security.py`

## Run
    python main.py

## Run tests
    pip install pytest
    pytest

## What I tested
- Correct and incorrect passwords (including a one-letter difference)
- Salts are random for every call
- Same password + same salt gives the same hash
- Manual testing: duplicate login, empty input, unknown user, wrong password.
  Several crashes found this way are fixed (missing user on login, duplicate registration).

## Limitations / TODO
- [ ] No brute-force
