class Bank:
    def __init__(self, acc_number, customer_name, balance=0):
        self.acc_number = acc_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Not enough balance!")

    def get_balance(self):
        return self.balance


# Example usage
account1 = Bank(101, "Adi", 500)   # create account with 500 balance

account1.deposit(200)              # add 200
account1.withdraw(100)             # take out 100
print("Final Balance:", account1.get_balance())  # check balance
