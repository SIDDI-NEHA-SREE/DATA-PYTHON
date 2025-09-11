#bank
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt
        return f"Deposit successful\nCurrent Balance - {self.__balance}"

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
            return f"Withdrawal successful\nCurrent Balance - {self.__balance}"
        else:
            return f"Withdrawal failed\nInsufficient Balance\nCurrent Balance - {self.__balance}"

    def get_balance(self):
        return f"Current Balance - {self.__balance}"
    
    
d=BankAccount()    
print(d.deposit(5000))
print(d.withdraw(2000))
print(d.get_balance())

