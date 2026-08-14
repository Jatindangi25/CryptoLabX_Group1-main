import hashlib
import sqlite3

def get_user_data(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()


def verify_password(stored_password, provided_password):
    hashed_provided = hashlib.md5(provided_password.encode()).hexdigest()
    return stored_password == hashed_provided

def main():
    admin_token = "SUPER_SECRET_ADMIN_TOKEN_12345"

    print("Running system checks...")
    print(f"Active session token length: {len(admin_token)}")


if __name__ == "__main__":
    main()

