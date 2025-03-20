class BankAccount:
    def __init__(self, account_name="", account_number=""):
        self.balance = 0.0
        self.transactions = []
        self.account_name = account_name
        self.account_number = account_number
        self.bills = {
            "Electricity": 150.00,
            "Water": 75.00,
            "Internet": 89.99,
            "Phone": 60.00,
            "Rent": 1200.00
        }
        self.paid_bills = []

    def __del__(self):
        print("\nThank you for banking with Strataconomics Bank.")

    def display_account_info(self):
        print(f"\n--- Account Information ---")
        print(f"Account Name: {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: M{self.balance:.2f}")
        print("-------------------------")

    def check_balance(self):
        print(f"\nYour current balance is M{self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("\nEnter the amount you would like to deposit: M"))
            if amount <= 0:
                print("\nPlease enter a positive amount.")
            else:
                self.balance += amount
                self.transactions.append(f"Deposit: +M{amount:.2f}")
                if len(self.transactions) > 5:  # Increased to keep last 5 transactions
                    self.transactions.pop(0)
                print(f"M{amount:.2f} has been deposited to your account.")
                print(f"\nUpdated balance: M{self.balance:.2f}")
        except ValueError:
            print("Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("\nEnter the amount you would like to withdraw: M"))
            if amount <= 0:
                print("\nPlease enter a positive amount.")
            elif amount > self.balance:
                print("\nYou have insufficient funds.")
            else:
                self.balance -= amount
                self.transactions.append(f"Withdrawal: -M{amount:.2f}")
                if len(self.transactions) > 5:
                    self.transactions.pop(0)
                print(f"\nM{amount:.2f} has been withdrawn from your account.")
                print(f"\nUpdated balance: M{self.balance:.2f}")
        except ValueError:
            print("Please enter a valid number.")

    def mini_statement(self):
        if not self.transactions:
            print("\nNo transactions available.")
        else:
            print("\n---Mini Statement---")
            for transaction in self.transactions[-5:]:  # Show last 5 transactions
                print(transaction)
            print("---------------------")

    def pay_bill(self):
        print("\n--- Available Bills ---")
        
        # Filter out already paid bills
        unpaid_bills = {name: amount for name, amount in self.bills.items() 
                       if name not in self.paid_bills}
        
        if not unpaid_bills:
            print("You have no pending bills to pay.")
            return
            
        # Display available bills to pay
        for idx, (bill_name, amount) in enumerate(unpaid_bills.items(), 1):
            print(f"{idx}. {bill_name}: M{amount:.2f}")
        
        try:
            choice = int(input("\nEnter the bill number you want to pay (0 to cancel): "))
            if choice == 0:
                print("Bill payment canceled.")
                return
                
            if 1 <= choice <= len(unpaid_bills):
                bill_name = list(unpaid_bills.keys())[choice-1]
                bill_amount = unpaid_bills[bill_name]
                
                if bill_amount > self.balance:
                    print(f"\nInsufficient funds to pay {bill_name} bill of M{bill_amount:.2f}")
                    print(f"Your current balance is M{self.balance:.2f}")
                else:
                    self.balance -= bill_amount
                    self.transactions.append(f"Bill Payment ({bill_name}): -M{bill_amount:.2f}")
                    self.paid_bills.append(bill_name)
                    
                    if len(self.transactions) > 5:
                        self.transactions.pop(0)
                        
                    print(f"\n{bill_name} bill of M{bill_amount:.2f} has been paid successfully.")
                    print(f"Updated balance: M{self.balance:.2f}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def register_account():
    print("\n--- Account Registration ---")
    account_name = input("Enter your full names: ")
    
    while True:
        account_number = input("Enter a 6-digit account number: ")
        if account_number.isdigit() and len(account_number) == 6:
            break
        print("Invalid account number. Please enter exactly 6 digits.")
    
    initial_deposit = 0
    try:
        initial_deposit = float(input("Enter initial deposit amount (optional): M"))
        if initial_deposit < 0:
            print("Cannot deposit a negative amount. Setting initial deposit to M0.")
            initial_deposit = 0
    except ValueError:
        print("Invalid amount. Setting initial deposit to M0.")
    
    account = BankAccount(account_name, account_number)
    if initial_deposit > 0:
        account.balance = initial_deposit
        account.transactions.append(f"Initial Deposit: +M{initial_deposit:.2f}")
    
    print("\nAccount registered successfully!")
    account.display_account_info()
    return account


def menu():
    print('\n---Strataconomics Bank---')
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini statement")
    print("5. Pay bills")
    print("6. Display account info")
    print("7. Exit")


def main():
    # Start with account registration
    account = register_account()
    
    while True:
        menu()
        try:
            menu_option = int(input("\nEnter your option (1-7): "))
            
            match menu_option:
                case 1:
                    account.check_balance()
                case 2:
                    account.deposit()
                case 3:
                    account.withdraw()
                case 4:
                    account.mini_statement()
                case 5:
                    account.pay_bill()
                case 6:
                    account.display_account_info()
                case 7:
                    print("\nExiting the banking system...")
                    # Explicitly calling the destructor
                    del account
                    break
                case _:
                    print("You have selected an invalid service, please try again.")
        except ValueError:
            print("Please enter a valid option (1-7).")


if __name__ == "__main__":
    main()