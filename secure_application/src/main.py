import sqlite3

# Database connection
conn = sqlite3.connect("atm.db")
cursor = conn.cursor()

# Create account table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id TEXT PRIMARY KEY,
    pin TEXT,
    balance REAL
)
""")

# Add demo account
cursor.execute(
    "INSERT OR IGNORE INTO accounts VALUES ('1001', '1234', 5000)"
)
conn.commit()

is_login = False
current_id = None


# ---------------- LOGIN ----------------
def login():
    global is_login, current_id

    account_id = input("Enter Account ID: ")
    pin = input("Enter PIN: ")

    try:
        query = (
            "SELECT * FROM accounts "
            "WHERE id='" + account_id +
            "' AND pin='" + pin + "'"
        )

        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            is_login = True
            current_id = user[0]
            print("Login successful!")
        else:
            print("Invalid Account ID or PIN.")

    except Exception as e:
        print("Database Error:", e)


# ---------------- BALANCE ----------------
def balance_inquiry():
    if not is_login:
        print("Please login first.")
        return

    try:
        cursor.execute(
            "SELECT balance FROM accounts WHERE id=?",
            (current_id,)
        )

        result = cursor.fetchone()

        if result:
            print("Current Balance:", result[0])

    except Exception as e:
        print("Error:", e)

# ---------------- WITHDRAW ----------------
def withdraw():
    if not is_login:
        print("Please login first.")
        return

    amount = input("Enter withdrawal amount: ")

    try:
        amount = float(amount)

        if amount <= 0:
            print("Invalid amount.")
            return

        cursor.execute(
            "SELECT balance FROM accounts WHERE id=?",
            (current_id,)
        )

        balance = cursor.fetchone()[0]

        if amount <= balance:
            new_balance = balance - amount

            cursor.execute(
                "UPDATE accounts SET balance=? WHERE id=?",
                (new_balance, current_id)
            )

            conn.commit()

            print("Withdrawal successful.")
            print("Remaining Balance:", new_balance)

        else:
            print("Insufficient balance.")

    except Exception as e:
        print("Withdrawal Error:", e)


# ---------------- DEPOSIT ----------------
def deposit():
    if not is_login:
        print("Please login first.")
        return

    amount = input("Enter deposit amount: ")

    try:
        amount = float(amount)

        if amount <= 0:
            print("Invalid amount.")
            return

        cursor.execute(
            "SELECT balance FROM accounts WHERE id=?",
            (current_id,)
        )

        balance = cursor.fetchone()[0]
        new_balance = balance + amount

        cursor.execute(
            "UPDATE accounts SET balance=? WHERE id=?",
            (new_balance, current_id)
        )

        conn.commit()

        print("Deposit successful.")
        print("New Balance:", new_balance)

    except Exception as e:
        print("Deposit Error:", e)


# ---------------- CHANGE PIN ----------------
def change_pin():
    if not is_login:
        print("Please login first.")
        return

    old_pin = input("Enter old PIN: ")
    new_pin = input("Enter new PIN: ")

    if old_pin == "" or new_pin == "":
        print("PIN cannot be empty.")
        return

    cursor.execute(
        "SELECT pin FROM accounts WHERE id=?",
        (current_id,)
    )

    result = cursor.fetchone()

    if result and result[0] == old_pin:
        cursor.execute(
            "UPDATE accounts SET pin=? WHERE id=?",
            (new_pin, current_id)
        )

        conn.commit()

        print("PIN changed successfully.")
    else:
        print("Incorrect old PIN.")


# ---------------- LOGOUT ----------------
def logout():
    global is_login, current_id

    is_login = False
    current_id = None

    print("Logged out successfully.")


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n========== ATM ==========")
        print("1. Login")
        print("2. Balance Inquiry")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Change PIN")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            login()

        elif choice == "2":
            balance_inquiry()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            deposit()

        elif choice == "5":
            change_pin()

        elif choice == "6":
            logout()

        elif choice == "7":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    menu()
