import sqlite3
import getpass

from security import verify_password

def run():
    login1 = input("Enter your login: ")
    password1 = getpass.getpass("Enter your password: ")

    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("SELECT salt, password_hash FROM users WHERE login = ?",
      (login1,)
    )
    row = cursor.fetchone()
    con.close()
    if row is None:
        print("Incorrect login or password.")
        return

    salt, stored_hash = row

    if verify_password(password1, salt, stored_hash):
        print("Welcome, " + login1 + "!")
    else:
        print("Incorrect login or password.")

if __name__ == "__main__":
    run()
