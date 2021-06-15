from bank_account import bankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        return self.account.display_account_info()

    def transfer_money(self, other_user, amount):
        if(other_user != None):
            self.account = self.account-amount
            other_user.make_deposit(amount)
            return self
        else:
            return print('Ingrese Usuario Valido')


# crear usuario/////////////////////////////////////////
carlitos = User('Carlitos Lechuga', 'carlechu@asd.asd')
juanin = User('Juanin Juan Harry', 'jujuha.asd@asd')
#print(carlitos.name, carlitos.email)
#print(juanin.name, juanin.email)
# movimientos///////////////////////////////////////////
carlitos.make_deposit(5000).display_user_balance()
carlitos.make_withdrawal(500).display_user_balance()
