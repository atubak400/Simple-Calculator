import sqlite3
import datetime
now = datetime.datetime.now()



class repo():
    def create_table(self):
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
        conn.commit()
        conn.close()

    def signup_custumer(self, email, firstname, lastname):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()    
        c.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)", (email, firstname, lastname, 0, now, "-"))
        conn.commit()
        conn.close()

    def get_customer(self, email):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customers WHERE Email = ?", (email,))
        item = c.fetchone()
        conn.commit()
        conn.close()
        return item
        
    def update_customer(self, new_amount, now, email):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE customers SET Balance = ?, Updated_at = ? WHERE Email = ?", (new_amount, now, email))
        conn.commit()
        conn.close()
        