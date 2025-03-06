# Define a class for the calculator
class Calculator:
    # Constructor to initialize the calculator
    def __init__(self):
        print("Simple Calculator initialized.")

    # Function to display the menu
    def menu(self):
        print('---Simple Calculator---')
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Exit")

    # Function for addition
    def add(self):
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        addition = a + b
        print(f"The result is: {addition}")

    # Function for subtraction
    def minus(self):
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        subtraction = a - b
        print(f"The result is: {subtraction}")

    # Function for division
    def divide(self):
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            division = a / b
            print(f"The result is: {division}")

    # Function for multiplication
    def multiple(self):
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        multiplication = a * b
        print(f"The result is: {multiplication}")

    # Function to run the calculator program
    def run(self):
        while True:
            self.menu()  # Display the menu
            menu_options = int(input("Enter your option (1-5): "))

            # Use match-case to handle user input
            match menu_options:
                case 1:
                    self.add()  # Call the addition function
                case 2:
                    self.minus()  # Call the subtraction function
                case 3:
                    self.divide()  # Call the division function
                case 4:
                    self.multiple()  # Call the multiplication function
                case 5:
                    print("Goodbye!")  # Exit the program
                    break
                case _:
                    print("You have entered an invalid option. Please try again.")  # Handle invalid input


# Main program
if __name__ == "__main__":
    calc = Calculator()  # Create an instance of the Calculator class
    calc.run()  # Run the calculator program