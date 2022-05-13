""""RULES, DEFAULTS, ASSERTIONS FOR CLASS DEFINITION ARGUMENTS"""
print("RULES, DEFAULTS, ASSERTIONS FOR CLASS DEFINITION ARGUMENTS")
print("")

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount  #ClassAttribute
    def __init__(self, name: str, price: float, quantity=0): #nsme must be a string, price must be an int/float, quatity is optional with a value of 0
        # Run Validation ti the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
print(item1.price)

item2 = Item("Laptop", 100, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)



import csv
print("")
""""RETURNING A LIST OF YOUR OBJECTS AND THEIR PROPERTIES"""
print("RETURNING A LIST OF YOUR OBJECTS AND THEIR PROPERTIES")
print("")

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount  #ClassAttribute
    all = []
    def __init__(self, name: str, price: float, quantity=0): #nsme must be a string, price must be an int/float, quatity is optional with a value of 0
        # Run Validation ti the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  #appends all instances into a list

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate



        for item in items:
            print(item)


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Mouse", 20, 5)
item4 = Item("Laptop", 50, 3)
item5 = Item("Laptop", 75, 5)

print(Item.all)

