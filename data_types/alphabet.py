def sort_characters():
    while True:
        chars = input("Enter characters separated by commas (or type 'exit' to quit): ")
        
        if chars.lower() == 'exit':
            print("Exiting the program.")
            break  # Stop the loop when user types exit/Exit/EXIT

        sorted_chars = sorted([char.strip() for char in chars.split(',')])

        print("Sorted characters:", ', '.join(sorted_chars))

sort_characters()