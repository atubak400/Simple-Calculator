import argparse
import model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("function", help="function", \
                choices=["create", "deposit", "transfer"]
                )

    parser.add_argument(
        "--email",
        type=str,
        help="Your email signup email address"
        )

    parser.add_argument(
        "--email1",
        type=str,
        help="Your email address that will be debited for the transfer"
        )

    parser.add_argument(
        "--email2",
        type=str,
        help="Email address of the Recieving Account"
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
        "--amount",
        type=int,
        help="amount to be deposited or transfered"
        )

    args = parser.parse_args()





if args.function == "create":
    customer = model.CustomerUsecase()
    customer.create_wallet(args.email, args.firstname, args.lastname)

if args.function == "deposit":
    customerss = model.CustomerUsecase()
    customerss.deposit(args.email, args.amount)

if args.function == "transfer":
    customerss = model.CustomerUsecase()
    customerss.transfer(args.email1, args.email2, args.amount)
    









"""    if args.function == "create":
        functions.create(args.email, args.firstname, args.lastname)
        model
    elif args.function == "deposit":
        functions.deposit(args.email, args.amount)
    elif args.function == "transfer":
        functions.transfer(args.email1, args.email2, args.amount)
    print("Try again with a valid email address and amount")"""

    

