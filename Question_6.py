import os

# Question 6.1

def read_entries():
    with open("students.txt", "r") as file:
        entries = file.read()
    print("\n--- Students & Scores ---")
    print(entries)

read_entries()

# Question 6.2

def calculate_average():
    with open("students.txt", "r") as file:
        scores = []
        for line in file:
            try:
                name, score = line.strip().split(",")
                scores.append(float(score))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
        if scores:
            average = sum(scores) / len(scores)
            print(f"\n--- Average Score ---\n{average:.2f}")
        else:
            print("\nNo valid scores to calculate an average.")

calculate_average()

# Question 6.3

def write_passed_students():
    with open("students.txt", "r") as infile, open("passed.txt", "w") as outfile:
        for line in infile:
            try:
                name, score = line.strip().split(",")
                if float(score) >= 50:
                    outfile.write(f"{name}\n")
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

write_passed_students()

# Question 6.4


if not os.path.exists("students.txt"):
    print("\nError: The file 'students.txt' does not exist. Please ensure the file is in the correct location.")
else:
    print("\nThe file 'students.txt' exists. Proceeding with operations.")