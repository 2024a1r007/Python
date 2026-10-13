#create a bank account class that stores an account holder's name and balance . add instance methods to deposit money, withdraw money, and display the balance. do not allow a  withdraw greater than the available balance

class bank_account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
    def display(self):
        print("name:",self.name)
        print("balance:",self.balance)