class Customer:
    
    def __init__(self, email: str, first_name: str, last_name: str, created_at, updated_at, balance: int = 0):
        self.email = email,
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.balance = balance
