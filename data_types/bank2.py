class BankAccount:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def __del__(self):
        print("\nThank you for banking with Strataconomics Bank.")

    def check_balance(self):
        print(f"\nYour current balance is ${self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("\nEnter the amount you would like to deposit: "))
            if amount < 0:
                print("\nThat's not a valid amount")
            else:
                self.balance += amount
                self.transactions.append(f"Deposit: +${amount:.2f}")
                if len(self.transactions) > 3:
                    self.transactions.pop(0)  # Keep only the last three transactions
                print(f"${amount:.2f} has been deposited to your account.")
        except ValueError:
            print("Please enter a valid number.")
            print(f"\nUpdated balance: ${self.balance:.2f}")
           

    def withdraw(self):
        try:
            amount = float(input("Enter the amount you would like to withdraw: "))
            if amount < 0:
                print("That's not a valid amount.")
            elif amount > self.balance:
                print("You have insufficient funds.")
            else:
                self.balance -= amount
                self.transactions.append(f"Withdrawal: -${amount:.2f}")
                if len(self.transactions) > 3:
                    self.transactions.pop(0)  # Keep only the last three transactions
                print(f"\n${amount:.2f} has been withdrawn from your account.")
        except ValueError:
            print("Please enter a valid number.")
        print(f"\nUpdated balance: ${self.balance:.2f}")

    def mini_statement(self):
        if not self.transactions:
            print("No transactions available.")
        else:
            print("\n---Mini Statement---")
            for transaction in self.transactions[-3:]:  # Show only the last three transactions
                print(transaction)
            print("---------------------")

def menu():
    print('\n---Strataconomics Bank---')
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini statement")
    print("5. Exit")

# Main program loop
account = BankAccount()

while True:
    menu()
    menu_options = int(input("Enter your option (1-5): "))

    match menu_options:
        case 1:
            account.check_balance()
        case 2:
            account.deposit()
        case 3:
            account.withdraw()
        case 4:
            account.mini_statement()
        case 5:
            print("Thank you for banking with us!!!")
            del account  # Explicitly calling the destructor
            break  # Exiting the loop and ending the program
        case _:
            print("You have selected an invalid service, please try again.")
