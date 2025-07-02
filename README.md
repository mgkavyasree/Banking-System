# HMBank - Banking System

This project implements a modular and extensible banking system in Python. It simulates a real-world banking environment supporting various account operations and customer services.

## Features and Functionalities

### 1. Account Management

* Create accounts (Savings, Current, Zero Balance)
* Auto-generated customer and account IDs
* View account details
* List all accounts
* List accounts sorted by customer name
* View unique account numbers

### 2. Transaction Services

* Deposit into an account
* Withdraw from an account
* Transfer funds between accounts
* Check account balance
* View transaction history (in-memory list)

### 3. Interest & Reporting

* Calculate and apply interest to savings accounts
* View accounts as list or key-value (map) format

### 4. Data Structures & Utilities

* Validate password strength (length, uppercase, number)
* Loan eligibility checker (based on credit score and income)
* Account balance loop check using dictionary
* Compound interest calculator for multiple customers

### 5. Exception Handling

* Custom exceptions:

  * InvalidAccountException
  * InsufficientFundException
  * OverdraftLimitExceededException
* Used in transactions and account operations

### 6. Input Validations

* Name validation (alphabetic only)
* Email format validation
* Phone number (10 digits)
* Positive numeric values for balances and transactions
* Valid account types enforced

### 7. Object-Oriented Design

* Encapsulated Customer and Account classes
* Inheritance for account types
* Interface-like structure using abstract methods
* Composition: Customer associated with Account

### 8. SQL Database Integration (Optional)

* Structured schema for Customers, Accounts, Transactions
* Auto-incremented primary keys
* Referential integrity with foreign keys

---

This system is suitable for training, demonstration, or as a foundation for more advanced banking applications.
