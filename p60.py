#create a product class with the product name , price, and quantity. add an instance method to calculate the total cost . take these values from the user and display the product name and total cost
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_cost(self):
        return self.price*self.quantity