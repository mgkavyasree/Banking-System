# Updated main_module.py to include 5 main categories and 25 menu options
from entity.customer import Customer
from service.bank_service_provider_impl import BankServiceProviderImpl
from exception.custom_exceptions import *

def main():
    bank = BankServiceProviderImpl()

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
                print("""
Account Management:
1. Create Account
2. Get Account Details
3. List Accounts
4. List Sorted Accounts
5. Unique Account Numbers
""")
                sub = input("Choose option: ")
                if sub == '1':
                    cid = input("Customer ID: ")
                    fname = input("First Name: ")
                    lname = input("Last Name: ")
                    email = input("Email: ")
                    phone = input("Phone: ")
                    address = input("Address: ")
                    customer = Customer(cid, fname, lname, email, phone, address)
                    acc_type = input("Account Type (savings/current/zero_balance): ").lower()
                    balance = float(input("Initial Balance: ")) if acc_type != "zero_balance" else 0.0
                    acc_no = bank.create_account(customer, acc_type, balance)
                    print(f"Account created successfully. Account No: {acc_no}")
                elif sub == '2':
                    acc_no = int(input("Account No: "))
                    bank.get_account_details(acc_no)
                elif sub == '3':
                    bank.list_accounts()
                elif sub == '4':
                    bank.list_accounts_sorted()
                elif sub == '5':
                    print(bank.unique_account_numbers())

            elif main_choice == '2':
                print("""
Transaction Services:
1. Deposit
2. Withdraw
3. Transfer
4. Get Balance
5. Transaction History
""")
                sub = input("Choose option: ")
                if sub == '1':
                    acc = int(input("Account No: "))
                    amt = float(input("Amount: "))
                    print("Balance:", bank.deposit(acc, amt))
                elif sub == '2':
                    acc = int(input("Account No: "))
                    amt = float(input("Amount: "))
                    print("Balance:", bank.withdraw(acc, amt))
                elif sub == '3':
                    from_acc = int(input("From Account: "))
                    to_acc = int(input("To Account: "))
                    amt = float(input("Amount: "))
                    bank.transfer(from_acc, to_acc, amt)
                    print("Transfer successful.")
                elif sub == '4':
                    acc = int(input("Account No: "))
                    print("Balance:", bank.get_account_balance(acc))
                elif sub == '5':
                    for t in bank.get_transaction_history():
                        print("-", t)

            elif main_choice == '3':
                print("""
Interest & Reporting:
1. Calculate Interest
2. Account List View
3. Account Map View
4. Report Generation
5. Export Data
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
                        print(f"Account No: {acc_no}")
                        acc.print_info()
                elif sub == '4':
                    print(bank.generate_report())
                elif sub == '5':
                    bank.export_data()
                    print("Data exported.")

            elif main_choice == '4':
                print("""
Data Structures & Utilities:
1. Password Validation
2. Loan Eligibility
3. Balance Loop Check
4. Compound Interest for Customers
5. Exit Utilities
""")
                sub = input("Choose option: ")
                if sub == '1':
                    pwd = input("Create your password: ")
                    print(bank.validate_password(pwd))
                elif sub == '2':
                    score = int(input("Enter credit score: "))
                    income = float(input("Enter annual income: "))
                    print(bank.check_loan_eligibility(score, income))
                elif sub == '3':
                    acc_no = input("Enter account number: ")
                    print(bank.loop_check_account(acc_no))
                elif sub == '4':
                    n = int(input("Enter number of customers: "))
                    for i in range(n):
                        bal = float(input("Initial balance: "))
                        rate = float(input("Interest rate: "))
                        yrs = int(input("Years: "))
                        print(f"Future balance: {bank.compound_interest(bal, rate, yrs):.2f}")
                elif sub == '5':
                    print("Returning to main menu.")

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
