#write a class for a bank account, a bank account should have an owner and a balance and shoule be able to deposit money and withdraw money
class BankAccount:
    rate = 0.02
    def __init__(self, owner, initial_balance = 0):
        self.owner = owner
        self.balance = initial_balance
    def deposit_money(self, value):
        self.balance += value
    def withdraw_money(self, value):
        if value > self.balance:
            print("insufficient funds")
        else:
            print(f'here is your ${value}.')
            self.balance -= value
    def get_balance(self):
        return self.balance
    def get_owner(self):
        return self.owner
    def set_owner(self, new_owner):
        self.owner = new_owner
    def __str__(self):
        return f'owner:{self.get_owner()}, balance: {self.get_balance()}'

    def __add__(self, other):
        new_owner = f'{self.get_owner()} & {other.get_owner()}'
        new_balance = self.get_balance() + other.get_balance()
        #new_account = f'owner: {new_owner}, and balance:{new_balance}' this uses a string which won't allow us to add to other accounts because they are BankAccount objects
        new_account = BankAccount(new_owner, new_balance)
        return new_account

    def __eq__(self, other):#assume at this bank you can only have one account, if the owner names are the same then it is the same account
        return self.get_owner() == other.get_owner()

    def give_interest(self):
        self.balance = self.balance + self.balance * self.rate




eric_acc = BankAccount('Eric')
eric_acc.deposit_money(100)
eric_acc.deposit_money(50)
#eric_acc.withdraw_money(25)
#print(eric_acc.get_balance())

ashley_acc = BankAccount('Ashley', 500)
ashley_acc.deposit_money(250)
#print(ashley_acc.get_balance())

#other_acc = BankAccount('???', 100)
ashley_acc.give_interest()
print(ashley_acc)


#print(ashley_acc)

#print(eric_acc == ashley_acc)
#print(eric_acc == eric_acc)
#other_acc_name = eric_acc


#joint_acc = eric_acc + ashley_acc
#print(joint_acc)

#print(newest_acc)


