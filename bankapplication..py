class Accont:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
# in the deposite method balance and amount were added
    def deposit(self,amount):
        self.balance=self.balance+ amount
# here how and when we have to withdraw amount
    def withdraw (self,amount):
        if self.balance-amount>=self.min_balance:self.balance=self.balance-amount
# when it was below the minimum balance
        else:
            print('sorry,insufficient balance')
# to saw total balance in account
    def print_statement(self):
        print('account balance:',self.balance)
# here Accout class for inherited
class Current (Accont):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return '{} current account balance.{}'.format(self.name,self.balance)
# Accout class were inherited
class Savings(Accont):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return '{} saving account balance.{}'.format(self.name,self.balance)
c=Savings('Jeevitha',20000)
print(c)
c.deposit(5000)
print(c)
c.print_statement()
c.withdraw(16000)
c.withdraw(20000)
print(c)
c2=Current('praveen',50000)
print(c2)
c2.deposit(10000)
print(c2)
c2.withdraw(20000)
c2.withdraw(50000)
print(c2)