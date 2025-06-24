# Banking system using oops
#

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        return "User Name: {} \nUser Age: {} \nGender: {}".format(self.name, self.age, self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        print("Depositing {} to account for {}".format(amount, self.name))
        self.balance += amount

    def withdraw(self, amount):
        print("Withdrawing {} from account of {}".format(amount, self.name))
        if amount > self.balance:
            print("Error! Insufficient balance. Kindly enter amount less than {}".format(self.balance))
        else:
            self.balance -= amount

    def get_balance(self):
        return "Balance is {}".format(self.balance)


raunak = Bank('Raunak', 34, 'Male')
print(raunak.user_details())
print(raunak.get_balance())
raunak.withdraw(500)
print(raunak.get_balance())
raunak.deposit(500)
print(raunak.get_balance())
raunak.withdraw(200)
print(raunak.get_balance())