class Account:
    last_acc_no = 1000

    def __init__(self, acc_type, balance, customer):
        Account.last_acc_no += 1
        self.acc_number = Account.last_acc_no
        self.acc_type = acc_type
        self.acc_balance = balance
        self.customer = customer

    def print_info(self):
        print(f"Account No: {self.acc_number}, Type: {self.acc_type}, Balance: {self.acc_balance}")
        self.customer.print_info()

class SavingsAccount(Account):
    def __init__(self, balance, customer):
        super().__init__('savings', max(balance, 500), customer)
        self.interest_rate = 4.5

    def calculate_interest(self):
        interest = self.acc_balance * self.interest_rate / 100
        self.acc_balance += interest

class CurrentAccount(Account):
    def __init__(self, balance, customer):
        super().__init__('current', balance, customer)
        self.overdraft_limit = 1000

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__('zero_balance', 0.0, customer)