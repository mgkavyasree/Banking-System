from entity.Account import SavingsAccount, CurrentAccount, ZeroBalanceAccount
from entity.Customer import Customer
from exception.Exceptions import *

class BankService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer, acc_type, balance):
        if acc_type == "savings":
            acc = SavingsAccount(balance, customer)
        elif acc_type == "current":
            acc = CurrentAccount(balance, customer)
        elif acc_type == "zero_balance":
            acc = ZeroBalanceAccount(customer)
        else:
            raise ValueError("Invalid account type")

        self.accounts[acc.acc_number] = acc
        return acc.acc_number

    def get_account_details(self, account_number):
        acc = self.accounts.get(account_number)
        if not acc:
            raise InvalidAccountException("Account not found")
        acc.print_info()

    def list_accounts(self):
        for acc in self.accounts.values():
            acc.print_info()

    def list_accounts_sorted(self):
        for acc in sorted(self.accounts.values(), key=lambda x: x.customer.first_name):
            acc.print_info()

    def unique_account_numbers(self):
        return set(self.accounts.keys())

    def get_account_balance(self, account_number):
        acc = self.accounts.get(account_number)
        if not acc:
            raise InvalidAccountException("Account not found")
        return acc.acc_balance

    def deposit(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if not acc:
            raise InvalidAccountException("Account not found")
        acc.acc_balance += amount
        return acc.acc_balance

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if not acc:
            raise InvalidAccountException("Account not found")
        if acc.acc_type == 'savings' and acc.acc_balance - amount < 500:
            raise InsufficientFundException("Minimum balance of 500 must be maintained")
        elif acc.acc_type == 'current' and acc.acc_balance - amount < -1000:
            raise OverdraftLimitExceededException("Overdraft limit exceeded")
        elif acc.acc_type == 'zero_balance' and acc.acc_balance < amount:
            raise InsufficientFundException("Insufficient balance")
        acc.acc_balance -= amount
        return acc.acc_balance

    def transfer(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            raise InvalidAccountException("One or both accounts not found")
        self.withdraw(from_acc, amount)
        return self.deposit(to_acc, amount)

    def calculate_interest(self):
        for acc in self.accounts.values():
            if isinstance(acc, SavingsAccount):
                acc.calculate_interest()

    def account_list(self):
        return list(self.accounts.values())

    def account_map(self):
        return dict(self.accounts)

    def is_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def is_valid_phone(phone):
        return re.match(r"^\d{10}$", phone)

    def is_valid_password(password):
        return (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password))

    def check_loan_eligibility():
        try:
            credit_score = int(input("Enter your credit score: "))
            income = float(input("Enter your annual income: "))
            if credit_score > 700 and income >= 50000:
                print("You are eligible for the loan.")
            else:
                print("You are not eligible for the loan.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    def balance_loop_check():
        accounts = {"1001": 5000.0, "1002": 3200.0, "1003": 7500.5, "1004": 12000.0, "1005": 2450.75}
        while True:
            acc = input("Enter your account number (or 'exit' to quit): ")
            if acc.lower() == 'exit':
                break
            if acc in accounts:
                print(f"Balance: ${accounts[acc]:.2f}")
            else:
                print("Invalid account number.")

    def compound_interest_calculator():
        try:
            num = int(input("Enter number of customers: "))
            for i in range(num):
                print(f"\nCustomer {i + 1}:")
                bal = float(input("Initial Balance: "))
                rate = float(input("Interest Rate (%): "))
                years = int(input("Years: "))
                future = bal * (1 + rate / 100) ** years
                print(f"Future balance: ${future:.2f}")
        except ValueError:
            print("Invalid input.")

    def is_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def is_valid_phone(phone):
        return re.match(r"^\d{10}$", phone)

    def is_valid_password(password):
        return (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password))

    def is_valid_name(name):
        return name.isalpha()

