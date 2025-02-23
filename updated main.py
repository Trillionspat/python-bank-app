###########################################################################################################################################
# PYTHON BANK APP (OOP) WITH INTEREST CALCULATION & SECURITY ENHANCEMENTS
###########################################################################################################################################

# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod


# Class Bank (Abstract Bank Class)
class Bank(ABC):
    def basicinfo(self):
        print('This is a generic bank')
        return 'Generic bank: 0'

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


# Class Swiss (A specific type of bank that derives from class Bank)
class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1_000

    def basicinfo(self):
        print('\n')
        print('This is your current Swiss Bank account')
        return f'Swiss Bank Amount: ${self.bal}'

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Withdrawn amount: ${amount}')
            print(f'New balance: ${self.bal}')
        else:
            print('Insufficient funds! Please try again.')
        return self.bal

    def deposit(self, amount):
        self.bal += amount
        print(f'Deposited amount: ${amount}')
        print(f'New Balance: ${self.bal}')
        return self.bal


# Savings Account with Interest Calculation
class Savings(Swiss):
    def __init__(self, interest_rate=0.02):
        super().__init__()
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.bal * self.interest_rate
        self.bal += interest
        print(f'Interest applied: ${interest:.2f}')
        print(f'New Balance after interest: ${self.bal:.2f}')
        return self.bal


# User Authentication Function
def authenticate():
    correct_pin = "1234"  # This should be securely stored in a real application
    for _ in range(3):
        pin = input("Enter your 4-digit PIN: ")
        if pin == correct_pin:
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN. Try again.")
    print("Too many failed attempts. Exiting...")
    return False


# Function to validate user input for amounts
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid input! Please enter a numerical value.")


# Driver Code
def main():
    assert issubclass(Bank, ABC), 'Bank must derive from class ABC'

    if not authenticate():
        return

    account_type = input("Select account type (C for Checking, S for Savings): ").strip().lower()

    if account_type == 's':
        account = Savings()
    else:
        account = Swiss()

    print(account.basicinfo())

    while True:
        print('\n')
        transaction = input('Do you want to make a transaction? (Y/N): ')
        if transaction.lower() == 'n':
            break
        elif transaction.lower() != 'y':
            print('Invalid input. Please type Y or N.')
            continue

        mode = input(
            'Please type W for Withdrawal, D for Deposit, or I to Apply Interest (Savings Only): ').strip().lower()

        if mode == 'w':
            amount = get_valid_amount()
            account.withdraw(amount)
        elif mode == 'd':
            amount = get_valid_amount()
            account.deposit(amount)
        elif mode == 'i' and isinstance(account, Savings):
            account.apply_interest()
        else:
            print('Error! Please enter W for Withdrawal, D for Deposit, or I for Interest (Savings Only).')


if __name__ == '__main__':
    main()
