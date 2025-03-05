# Function to display the menu
def menu():
    print('---Simple Calculator---')
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")

# Function for addition
def add():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    addition = a + b
    print(f"The result is: {addition}")

# Function for subtraction
def minus():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    subtraction = a - b
    print(f"The result is: {subtraction}")

# Function for division
def divide():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        division = a / b
        print(f"The result is: {division}")

# Function for multiplication
def multiple():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    multiplication = a * b
    print(f"The result is: {multiplication}")

# program loop
while True:
    menu()
    menu_options = int(input("Enter your option (1-5): "))

    # if menu_options < 1 or menu_options > 5:
    #     print("You have entered an invalid options. Please try again.")
    #     continue  # Go back to the menu

    match menu_options:
        case 1:
            add()
        case 2:
            minus()
        case 3:
            divide()
        case 4:
            multiple()
        case 5:
            print("Goodbye!")
            break  # Exit the loop and end the program
        case _: 
             print("You have entered an invalid option. Please try again.")