# Question 4.1

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_attribute(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)

    def remove_attribute(self, attr_name):
        if hasattr(self, attr_name):
            delattr(self, attr_name)

    def display_attributes(self):
        return self.__dict__
    
# Question 4.2
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_attribute(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)

    def remove_attribute(self, attr_name):
        if hasattr(self, attr_name):
            delattr(self, attr_name)

    def display_attributes(self):
        return self.__dict__


student = Student(1, "Keabetsoe Kuenene")
student.add_attribute("student_class", "Grade X")
print("Attributes after adding student_class:", student.display_attributes())

student.remove_attribute("student_name")
print("Attributes after removing student_name:", student.display_attributes())