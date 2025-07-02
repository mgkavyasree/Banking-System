from entity.Customer import Customer
from dao.BankService import BankService
from exception.Exceptions import (
    InvalidAccountException,
    InsufficientFundException,
    OverdraftLimitExceededException
)
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.match(r"^\d{10}$", phone)

def is_valid_password(password):
    return (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password))

def is_valid_name(name):
    return name.isalpha()

def main():
    bank = BankService()
    transactions = []

    while True:
        print("""
Main Menu:
1. Account Management
2. Transaction Services
3. Interest & Reporting
4. Data Structures & Utilities
5. Exit
""")
        main_choice = input("Enter your main menu choice (1-5): ")

        try:
            if main_choice == '1':
                while True:
                    print("""
Account Management:
1. Create Account
2. Get Account Details
3. List Accounts
4. List Sorted Accounts
5. Unique Account Numbers
6. Exit to Main Menu
""")
                    sub = input("Choose option: ")
                    if sub == '1':
                        while True:
                            fname = input("first name: ").strip()
                            if fname and is_valid_name(fname):
                                break
                            print("Invalid first name.")

                        while True:
                            lname = input("last name: ").strip()
                            if lname and is_valid_name(lname):
                                break
                            print("Invalid last name.")

                        while True:
                            email = input("email: ").strip()
                            if is_valid_email(email):
                                break
                            print("Invalid email format.")

                        while True:
                            phone = input("phone number (10 digits): ").strip()
                            if is_valid_phone(phone):
                                break
                            print("Invalid phone number.")

                        address = input("address: ").strip()
                        customer = Customer(None, fname, lname, email, phone, address)

                        while True:
                            acc_type = input("account_type (savings/current/zero_balance): ").lower()
                            if acc_type in ['savings', 'current', 'zero_balance']:
                                break
                            print("Invalid account type.")

                        balance = 0.0
                        if acc_type != "zero_balance":
                            while True:
                                try:
                                    balance = float(input("balance: "))
                                    if balance >= 0:
                                        break
                                    print("Balance cannot be negative.")
                                except ValueError:
                                    print("Invalid balance amount.")

                        acc_no = bank.create_account(customer, acc_type, balance)
                        print(f"Account created successfully. account_id: {acc_no}")

                    elif sub == '2':
                        try:
                            acc_no = int(input("account_id: "))
                            bank.get_account_details(acc_no)
                        except ValueError:
                            print("Account ID must be numeric.")

                    elif sub == '3':
                        bank.list_accounts()

                    elif sub == '4':
                        bank.list_accounts_sorted()

                    elif sub == '5':
                        print(bank.unique_account_numbers())

                    elif sub == '6':
                        break

                    else:
                        print("Invalid option.")

            elif main_choice == '2':
                while True:
                    print("""
Transaction Services:
1. Deposit
2. Withdraw
3. Transfer
4. Get Balance
5. Transaction History
6. Exit to Main Menu
""")
                    sub = input("Choose option: ")
                    if sub == '1':
                        try:
                            acc = int(input("account_id: "))
                            amt = float(input("amount: "))
                            if amt <= 0:
                                print("Amount must be positive.")
                                continue
                            transactions.append(f"Deposit to {acc}: ${amt}")
                            print("Balance:", bank.deposit(acc, amt))
                        except ValueError:
                            print("Invalid input.")

                    elif sub == '2':
                        try:
                            acc = int(input("account_id: "))
                            amt = float(input("amount: "))
                            if amt <= 0:
                                print("Amount must be positive.")
                                continue
                            transactions.append(f"Withdraw from {acc}: ${amt}")
                            print("Balance:", bank.withdraw(acc, amt))
                        except ValueError:
                            print("Invalid input.")

                    elif sub == '3':
                        try:
                            from_acc = int(input("from account_id: "))
                            to_acc = int(input("to account_id: "))
                            amt = float(input("amount: "))
                            if amt <= 0:
                                print("Amount must be positive.")
                                continue
                            bank.transfer(from_acc, to_acc, amt)
                            transactions.append(f"Transfer ${amt} from {from_acc} to {to_acc}")
                            print("Transfer successful.")
                        except ValueError:
                            print("Invalid input.")

                    elif sub == '4':
                        try:
                            acc = int(input("account_id: "))
                            print("Balance:", bank.get_account_balance(acc))
                        except ValueError:
                            print("Invalid account ID.")

                    elif sub == '5':
                        print("\nTransaction History:")
                        for t in transactions:
                            print("-", t)

                    elif sub == '6':
                        break
                    else:
                        print("Invalid option.")

            elif main_choice == '3':
                while True:
                    print("""
Interest & Reporting:
1. Calculate Interest
2. Account List View
3. Account Map View
4. Exit to Main Menu
""")
                    sub = input("Choose option: ")
                    if sub == '1':
                        bank.calculate_interest()
                        print("Interest applied.")
                    elif sub == '2':
                        for acc in bank.account_list():
                            acc.print_info()
                    elif sub == '3':
                        for acc_no, acc in bank.account_map().items():
                            print(f"account_id: {acc_no}")
                            acc.print_info()
                    elif sub == '4':
                        break
                    else:
                        print("Invalid option.")

            elif main_choice == '4':
                while True:
                    print("""
Data Structures & Utilities:
1. Password Validation
2. Loan Eligibility
3. Balance Loop Check
4. Compound Interest
5. Exit Utilities
""")
                    sub = input("Choose option: ")
                    if sub == '1':
                        pw = input("Create Password: ")
                        if is_valid_password(pw):
                            print("Password is valid.")
                        else:
                            print("Password must be 8+ chars with 1 uppercase and 1 digit.")
                    elif sub == '2':
                        from util.LoanEligibility import check_loan_eligibility
                        check_loan_eligibility()
                    elif sub == '3':
                        from util.BalanceChecker import balance_loop_check
                        balance_loop_check()
                    elif sub == '4':
                        from util.CompoundInterest import compound_interest_calculator
                        compound_interest_calculator()
                    elif sub == '5':
                        break
                    else:
                        print("Invalid option.")

            elif main_choice == '5':
                print("Exiting application.")
                break

            else:
                print("Invalid main menu choice.")

        except (InvalidAccountException, InsufficientFundException, OverdraftLimitExceededException) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected Error:", e)

if __name__ == "__main__":
    main()
