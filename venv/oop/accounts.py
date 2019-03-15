import datetime
import pytz


class Account:
    """Simple account class with balance"""

    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), self.__balance)]
        print("Account created for {} with {} balance".format(self._name, self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than 0 and not more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    # raunak = Account("Raunak", 0)
    # raunak.deposit(1000)
    # raunak.withdraw(250)
    # raunak.show_transactions()

    mahesh = Account("Mahesh", 2000)
    mahesh.deposit(1000)
    mahesh.withdraw(250)
    mahesh.show_transactions()
    mahesh.__balance = 300
    mahesh.show_balance()
    print(mahesh.__dict__)
