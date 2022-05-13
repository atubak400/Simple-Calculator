import sqlite3
import datetime
now = datetime.datetime.now()


conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS customers(
Email text unique,
First_name text,
Last_name text,
Balance integer,
Created_at timestamp,
Updated_at timestamp
)""")


class CustomerUsecase:

    def create_wallet(self, email, firstname, lastname):        
        c.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)", (email, firstname, lastname, 0, now, "-"))
        conn.commit()
        conn.close()
    
    def deposit(self, email, amount):
        c.execute("SELECT * FROM customers WHERE Email = ?", (email,))
        item = c.fetchone()
        new_amount = item[3] + amount
        c.execute("UPDATE customers SET Balance = ?, Updated_at = ? WHERE Email = ?", (new_amount, now, email))
        conn.commit()
        conn.close()
        print(f"Transaction successfull. You deposited {amount} Naira into your account!!")
        print(f"Your new balance is {new_amount} Naira.")

    def transfer(self, email1, email2, amount):
        updated_at = now
        c.execute("SELECT * FROM customers WHERE Email = ?", (email1,))
        item = c.fetchone()
        if item[3] >= amount:
            new_amount1 = item[3] - amount
        else:
            print("Insufficient Funds. Please recharge your account and try again!!")
        c.execute("UPDATE customers SET Balance = ?, Updated_at = ? WHERE Email = ?", (new_amount1, now, email1))
        c.execute("SELECT * FROM customers WHERE Email = ?", (email2,))
        items = c.fetchall()
        for item in items:
            new_amount2 = item[3] + amount
        c.execute("UPDATE customers SET Balance = ?, Updated_at = ? WHERE Email = ?", (new_amount2, updated_at, email2))
        conn.commit()
        conn.close()
        print(f"Transaction successfull. You transfered {amount} Naira into {email2}'s account!!")
        print(f"Your new balance is {new_amount1} Naira.")


