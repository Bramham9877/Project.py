import datetime

class Transaction:
    def __init__(self, type, amount):
        self.type = type  # 'Deposit' or 'Withdraw'
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.type}: ${self.amount:.2f}"

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(Transaction('Deposit', amount))
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append(Transaction('Withdraw', amount))
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def show_transactions(self):
        print(f"\nTransaction history for {self.holder_name}:")
        for tx in self.transactions:
            print(tx)

def main():
    accounts = {}

    while True:
        print("\n--- Bank Transaction Management ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Show Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            if acc_num in accounts:
                print("Account already exists!")
                continue
            accounts[acc_num] = BankAccount(acc_num, name)
            print("Account created successfully!")

        elif choice == '2':
            acc_num = input("Enter account number: ")
            if acc_num not in accounts:
                print("Account not found.")
                continue
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_num].deposit(amount)

        elif choice == '3':
            acc_num = input("Enter account number: ")
            if acc_num not in accounts:
                print("Account not found.")
                continue
            amount = float(input("Enter amount to withdraw: "))
            accounts[acc_num].withdraw(amount)

        elif choice == '4':
            acc_num = input("Enter account number: ")
            if acc_num not in accounts:
                print("Account not found.")
                continue
            accounts[acc_num].check_balance()

        elif choice == '5':
            acc_num = input("Enter account number: ")
            if acc_num not in accounts:
                print("Account not found.")
                continue
            accounts[acc_num].show_transactions()

        elif choice == '6':
            print("Thank you for using the Bank Transaction Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()