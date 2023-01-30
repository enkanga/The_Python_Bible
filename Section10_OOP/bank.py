
class Account:
    def __init__(self, name, account_type, balance, min_balance):
        self.name, self.account_type, self.balance, self.min_balance = name, account_type, balance, min_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            self.statement()
        else:
            print('Sorry, not enough funds!')
    
    def statement(self):
        print('Account Balance: £{}'.format(self.balance))

    def __str__(self):
        if (self.name[-1]).lower() == 's':
            return "{}' {} Account: Balance = £{}".format(self.name, self.account_type, self.balance) 
        else:
            return "{}'s {} Account: Balance = £{}".format(self.name, self.account_type, self.balance) 


class Current(Account):
    def __init__(self, name, balance, account_type = 'Current'):
        super().__init__(name, account_type, balance, min_balance = -1000)

class Savings(Account):
    def __init__(self, name, balance, account_type = 'Savings'):
        super().__init__(name, account_type, balance, min_balance = 0)

E = Current('Evelyn', 500)
T = Savings('Tobias', 300)