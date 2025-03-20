# Define the Student class
class Student:
    def __init__(self, student_name, student_id):
        """
        Initialize a Student object with a name, ID, and an empty list of courses.
        """
        self.student_name = student_name  # Student's name
        self.student_id = student_id  # Student's unique ID
        self.courses = []  # List to store courses as tuples (course_name, grade)

    def enroll_course(self, course_name, grade):
        """
        Enroll the student in a course by adding the course name and grade to the courses list.
        """
        self.courses.append((course_name, grade))  # Add a tuple (course_name, grade) to the list

    def display_details(self):
        """
        Display the student's details including name, ID, and enrolled courses with grades.
        """
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:")
        for course in self.courses:
            print(f"  - {course[0]}: {course[1]}")  # Print each course and its grade


# Define the StudentManagementSystem class
class StudentManagementSystem:
    def __init__(self):
        """
        Initialize the Student Management System with an empty list of students.
        """
        self.students = []  # List to store all Student objects

    def add_student(self, student_name, student_id):
        """
        Add a new student to the system by creating a Student object and adding it to the students list.
        """
        new_student = Student(student_name, student_id)  # Create a new Student object
        self.students.append(new_student)  # Add the student to the list
        print(f"Student {student_name} with ID {student_id} added successfully.")

    def enroll_student(self, student_id, course_name, grade):
        """
        Enroll a student in a course by finding the student by ID and calling their enroll_course method.
        """
        for student in self.students:
            if student.student_id == student_id:  # Check if the student ID matches
                student.enroll_course(course_name, grade)  # Enroll the student in the course
                print(f"Student {student.student_name} enrolled in {course_name} with grade {grade}.")
                return
        print(f"Student with ID {student_id} not found.")  # If student not found

    def view_student_details(self, student_id):
        """
        Display the details of a specific student by finding them by ID and calling their display_details method.
        """
        for student in self.students:
            if student.student_id == student_id:  # Check if the student ID matches
                student.display_details()  # Display the student's details
                return
        print(f"Student with ID {student_id} not found.")  # If student not found

    def list_all_students(self):
        """
        List all registered students by iterating through the students list and displaying their names and IDs.
        """
        if not self.students:
            print("No students registered.")
        else:
            print("Registered Students:")
            for student in self.students:
                print(f"  - {student.student_name} (ID: {student.student_id})")


# Main program
def main():
    """
    Main function to run the Student Management System with a menu-driven interface.
    """
    sms = StudentManagementSystem()  # Create an instance of the StudentManagementSystem

    while True:
        # Display the menu options
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. Enroll a student in a course")
        print("3. View a student's details")
        print("4. List all students")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == "1":
            # Add a new student
            student_name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            sms.add_student(student_name, student_id)

        elif choice == "2":
            # Enroll a student in a course
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = input("Enter grade: ")
            sms.enroll_student(student_id, course_name, grade)

        elif choice == "3":
            # View a student's details
            student_id = input("Enter student ID: ")
            sms.view_student_details(student_id)

        elif choice == "4":
            # List all students
            sms.list_all_students()

        elif choice == "5":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")


# Run the main program
if __name__ == "__main__":
    main()