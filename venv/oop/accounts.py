class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for {} with {} balance".format(self.name, self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than 0 and not more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    raunak = Account("Raunak", 0)
    raunak.deposit(1000)
    raunak.withdraw(250)

