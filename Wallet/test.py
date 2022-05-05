import argparse
import sqlite3

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("function", help="function", \
                choices=["create", "deposit", "transfer"]
                )

    parser.add_argument(
        "--email",
        type=str,
        help="Primary key for database identification"
        )

    parser.add_argument(
        "--firstname",
        type=str,
        help="fill your first name"
        )

    parser.add_argument(
        "--lastname",
        type=str,
        help="fill your second name"
        )

    args = parser.parse_args()

  
    def create(email, firstname, lastname):

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS new_customers(
        email text unique,
        first_name text,
        last_name text
        )""")
        try:
            c.execute("INSERT INTO new_customers VALUES (?,?,?)", (email, firstname, lastname))
        except:
            print("Sorry email already taken!!")
        c.execute("SELECT rowid, * FROM new_customers")
        items = c.fetchall()
        for item in items:
            print(item)
        conn.commit()
        conn.close()
        
    if args.function == "create":
        create(args.email, args.firstname, args.lastname)

    

