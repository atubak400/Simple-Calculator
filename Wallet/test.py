import argparse

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
        return f"My email is {email} and my full name is {firstname} {lastname}" 
    if args.function == "create":
        result = create(args.email, args.firstname, args.lastname)

    
    print(result)
    

