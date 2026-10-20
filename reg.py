import hashlib
import os
import sqlite3
import getpass

def run():
    login = input("Write your login: ").strip()
    password = getpass.getpass("Write your password: ")

    if not login or password:
        print("Login and password cannot be empty.")
        return


    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)

    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        login TEXT UNIQUE,
        salt BLOB,
        password_hash BLOB
    )""")
    con.commit()

    try:
        cursor.execute("INSERT INTO users VALUES(?,?,?)",
                (login, salt, password_hash)
        )
        con.commit()
        print("You have been registered!")
    except sqlite3.IntegrityError:
        print("This login is already taken.")
    finally:
        con.close()

if __name__ == "__main__":
    run()
