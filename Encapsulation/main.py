class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    print("Initial balance:", account.get_balance())  # Output: Initial balance: 1000
    
    account.deposit(500)  # Output: Deposited $500. New balance: $1500
    account.withdraw(200)  # Output: Withdrew $200. New balance: $1300
    
    print("Final balance:", account.get_balance())  # Output: Final balance: 1300
