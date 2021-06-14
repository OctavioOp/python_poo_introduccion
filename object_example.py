class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0 #valor por defecto
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance = self.account_balance - amount
        return self
    def display_user_balance(self):
        mount = str(self.account_balance)
        return print(f"el/la señor/ita {self.name}, posee en su cuenta: $ {mount}")
    def transfer_money(self, other_user, amount):
        if(other_user != None):
            self.account_balance = self.account_balance-amount
            other_user.make_deposit(amount)
            return self
        else:
            return print('Ingrese Usuario Valido')
        
        
#crear usuario/////////////////////////////////////////
carlitos = User('Carlitos Lechuga', 'carlechu@asd.asd')
juanin = User('Juanin Juan Harry', 'jujuha.asd@asd')
#print(carlitos.name, carlitos.email)
#print(juanin.name, juanin.email)
#movimientos///////////////////////////////////////////
carlitos.make_deposit(5000).display_user_balance()
juanin.make_deposit(100).display_user_balance()
print('--momento--transferencia--')
carlitos.transfer_money(juanin, 2000)
juanin.display_user_balance()
carlitos.display_user_balance()


