import datetime
import repository
now = datetime.datetime.now()




class CustomerUsecase():

    def create_wallet(self, email, firstname, lastname):        
        repository.repo.create_table(self)
        repository.repo.signup_custumer(self, email, firstname, lastname)
    
    def deposit(self, email, amount):
        item = repository.repo.get_customer(self, email)
        new_amount = item[3] + amount
        repository.repo.update_customer(self, new_amount, now, email)
        print(f"Transaction successfull. You deposited {amount} Naira into your account!!")
        print(f"Your new balance is {new_amount} Naira.")

    def transfer(self, email1, email2, amount):
        item = repository.repo.get_customer(self, email1)
        if item[3] >= amount:
            email1_new_amount = item[3] - amount
        else:
            print("Insufficient Funds. Please recharge your account and try again!!")
        repository.repo.update_customer(self, email1_new_amount, now, email1)
        item = repository.repo.get_customer(self, email2)
        email2_new_amount = item[3] + amount
        repository.repo.update_customer(self, email2_new_amount , now, email2)
        print(f"Transaction successfull. You transfered {amount} Naira into {email2}'s account!!")
        print(f"Your new balance is {email1_new_amount} Naira.")


