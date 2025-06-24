# import Exception

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        return "Name: {}, Age: {}, Gender: {}".format(self.name, self.age, self.gender)

class Account(User):
    def __init__(self, name, age, gender, balance=0):
        super().__init__(name, age, gender)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error! Balance not enough. Available balance is: {}".format(self.balance))
            raise InsufficientFundsException("Insufficient Funds", 300)
        else:
            self.balance -= amount

    def account_balance(self):
        return "{} has Rs.{} in his account currently".format(self.name, self.balance)

class InsufficientFundsException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message, error_code)
    
    def __str__(self):
        return "{} (Error Code: {})".format(message, error_code)


user_1 = Account("Raunak", 36, "M", balance=50000)
user_2 = Account("Monika", 36, "F")

print(user_1.account_balance())
print(user_2.account_balance())
user_1.deposit(20000)
user_2.deposit(60000)
print(user_1.account_balance())
print(user_2.account_balance())
user_1.withdraw(30000)
user_2.withdraw(50000)
print(user_1.account_balance())
print(user_2.account_balance())
user_2.withdraw(30000)
print(user_1.account_balance())
print(user_2.account_balance())




