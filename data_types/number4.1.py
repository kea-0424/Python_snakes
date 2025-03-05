def get_day_of_week():
    try:
        day_number = int(input("Enter a number (1-7): "))
        if day_number < 1 or day_number > 7:
            print("Please enter a valid number between 1 and 7.")
            get_day_of_week()  # Recursive call to prompt again
            return

        match day_number:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        get_day_of_week()  # Recursive call to prompt again

get_day_of_week()