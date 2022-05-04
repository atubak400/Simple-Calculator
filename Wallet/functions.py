import sqlite3

def create(email, firstname, lastname):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS customers(
    email text,
    first_name text,
    last_name text
    )""")
    c.execute("INSERT INTO customers VALUES (?,?,?)", (email, firstname, lastname))
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
        