import random
class bankAccount:
    def __init__(self, intRate=0.01, balance=0):
        self.intRate = intRate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print('Transacction approved, Thanks come again!')
            return self
        else:
            return print(
                'Not enough money, please add money to your account to proceed with the transacction')

    def display_account_info(self):
        return print(f'Sr@  you have $:  {self.balance}')

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.intRate)
        return self

#newAccount = bankAccount()
# newAccount.deposit(5000).yield_interest().display_account_info()
# newAccount.withdraw(3000).display_account_info()

