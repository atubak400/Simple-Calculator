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

    print(args.function)
    print(args.email)
    print(args.firstname)
    print(args.lastname)

  
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
        
    if args.function == "create":
        create(args.email, args.firstname, args.lastname)

    

