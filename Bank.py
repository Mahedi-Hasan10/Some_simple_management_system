class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Thank you for banking with us!!')

    def withdraw(self, amount):
        if (amount > self.min_withdraw):
            self.balance -= amount
            print(f'Withdraw amount : {amount}')
            print(f'Withdraw successful')
            print(f'Balance after withdraw : {self.balance}')
        elif amount < self.min_withdraw:
            print(
                f'Sala gorib tui {self.min_withdraw} takar niche withdraw korte parbi na')
        elif amount > self.max_withdraw:
            print(f'Bank fokir hoye jabe')


ibbl = Bank(15000)
ibbl.deposit(5000)
print(ibbl.get_balance())

ibbl.withdraw(50)
ibbl.withdraw(5000)
