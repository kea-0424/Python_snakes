# Question 6.1

import os as os

def read_file():
    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as file:
            file_content = file.read()
        print(f"File content:{file_content}")
    else:
        print("Error: 'students.txt' does not exist.")
