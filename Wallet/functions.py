import sqlite3
import datetime

now = datetime.datetime.now()

def create(email, firstname, lastname):
    created_at = (now.strftime("%y-%m-%d, %H:%M:%S"))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS customers(
    Email text unique,
    First_name text,
    Last_name text,
    Balance integer,
    Created_at integer,
    Updated_at integer
    )""")
    try:
        c.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)", (email, firstname, lastname, 0, created_at, "-"))
    except:
        print(f"Sorry, {email} is already taken!!")
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def deposit(email, amount):
    updated_at = (now.strftime("%y-%m-%d, %H:%M:%S"))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE Email = ?", (email,))
    items = c.fetchall()
    for item in items:
        new_amount = (item[3] + amount)
    c.execute("UPDATE customers SET Balance = ?, Updated_at = ? WHERE Email = ?", (new_amount, updated_at,email))
    conn.commit()
    conn.close()
    print(f"Transaction successfull. You deposited {amount} Naira into your account!!")
    print(f"Your new balance is {new_amount} Naira.")

        