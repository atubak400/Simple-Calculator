import datetime
from .repository import CustomerRepoInterface
now = datetime.datetime.now()



class CustomerUsecase:

    def __init__(self, customer_repo: CustomerRepoInterface):
        self.__customer_repo = customer_repo

    def create_wallet(self, email, firstname, lastname):        
        self.__customer_repo.create_table()
        self.__customer_repo.create_customer(email, firstname, lastname)
    
    def deposit(self, email, amount):
        customer = self.__customer_repo.get_customer(email)
        new_amount = customer.balance + amount
        self.__customer_repo.update_customer(email, new_amount, now)
        print(f"Transaction successfull. You deposited {amount} Naira into your account!!")
        print(f"Your new balance is {new_amount} Naira.")

    def transfer(self, sender_email, receiver_email, amount):
        sender = self.__customer_repo.get_customer(sender_email)
        if sender.balance >= amount:
            sender_new_balance = sender.balance - amount
        else:
            print("Insufficient Funds. Please recharge your account and try again!!")
        self.__customer_repo.update_customer(sender_email, sender_new_balance, now)
        receiver = self.__customer_repo.get_customer(receiver_email)
        receiver_new_balance = receiver.balance + amount
        self.__customer_repo.update_customer(receiver_email, receiver_new_balance , now)
        print(f"Transaction successfull. You transfered {amount} Naira into {receiver_email}'s account!!")
        print(f"Your new balance is {sender_new_balance} Naira.")



