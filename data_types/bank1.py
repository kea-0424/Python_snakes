

    # function to display the menu
def menu():
    print('\n---Strataconomics Bank---')
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini statement")
    print("5. Exit")
    
balance = 0.0
transactions = []


    # function for checking your balance
def check_balance():

    print(f"\nYour current balance is ${balance:.2f}")


     # function for depositing money 
def  deposit():
    global balance
    amount = float(input("\nEnter the amount you would like to deposit: "))

    if amount < 0:
        print("\nThat's not a valid amount")
    else:
        balance += amount
        transactions.append(f"Deposit: +${amount:.2f}")
        if len(transactions) > 3:
            transactions.pop(0)  # Keep only the last three transactions
        print(f"${amount:.2f} has been deposited to your account.")   
    



    
    # function for withdrawing 

def withdraw():
    global balance
    amount = float(input("Enter the amount you would like to withdraw: "))

    # Debugging: Print the current balance
    print(f"Current balance: ${balance:.2f}")

    if amount < 0:
        print("That's not a valid amount.")
    elif amount > balance:
        print("You have insufficient funds.")
    else:
        balance -= amount
        transactions.append(f"Withdrawal: -${amount:.2f}")
        if len(transactions) > 3:
            transactions.pop(0)  # Keep only the last three transactions
        print(f"\n${amount:.2f} has been withdrawn from your account.")

    # Debugging: Print the updated balance
    print(f"\nUpdated balance: ${balance:.2f}")




    # function of viewing past transctions 
def mini_statement(): 
        if not transactions:
            print("No transactions available.")
        else:
             print("\n---Mini Statement---")
        for transaction in transactions[-3:]:  # Show only the last three transactions
            print(transaction)
            print("---------------------")




# program loop
while True:
    menu()
    menu_options = int(input("Enter your option(1-5): "))

    match menu_options:
        case 1: 
            check_balance()

        case 2: 
            deposit()

        case 3:
            withdraw()
        
        
        case 4:
            mini_statement()


        case 5:
            print("Thank you for banking with us!!!")
            break #exiting the loop and ending the program

        case _:
            print("You have selected a invalid service, please try again.")

            
          

