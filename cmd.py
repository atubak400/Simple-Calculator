import argparse
from Wallet.usecase import CustomerUsecase
from Wallet.repository import CustomerRedisRepo, CustomerSqliteRepo

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


repo = CustomerRedisRepo()
#repo = CustomerSqliteRepo() #switch to sqlite
customer = CustomerUsecase(customer_repo=repo) 

if args.function == "create":
    customer.create_wallet(args.email, args.firstname, args.lastname)

if args.function == "deposit":
    customer.deposit(args.email, args.amount)

if args.function == "transfer":
    customer.transfer(args.email1, args.email2, args.amount)
