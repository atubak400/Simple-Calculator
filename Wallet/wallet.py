import argparse
import sqlite3
import functions

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

    parser.add_argument(
        "--user",
        type=str,
        help="email to receive deposit"
        )

    parser.add_argument(
        "--amount",
        type=int,
        help="amount to be deposited or transfered"
        )

    args = parser.parse_args()


    if args.function == "create":
        functions.create(args.email, args.firstname, args.lastname)

    elif args.function == "deposit":
        functions.deposit(args.email, args.amount)

    

