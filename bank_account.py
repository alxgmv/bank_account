class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self) -> str:
        return f"Account holder: {self.owner}"
    def deposit(self, amount):
        return self.balance + amount
    def withdraw(self, amount):
        if self.balance - amount < 0:
            return 'Not enough money to withdraw'
        else:
            return self.balance - amount