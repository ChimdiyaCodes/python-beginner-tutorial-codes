class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def greet(self):
        return f"Hello, my name is {self.firstname} {self.lastname}."

    def walk(self):
        return "I am walking."


class Student(Person):
    def __init__(self, fname, lname, major):
        super().__init__(fname, lname)  # Keep parent's __init__()
        self.major = major  # New attribute only in Student

    def study(self):
        return f"{self.firstname} is studying {self.major}."

    def walk(self):  # Overriding parent's walk method
        return "I am walking to class."


# Creating an instance of Student
student1 = Student("Chimdiya", "Iheke", "Medicine and Surgery")

# Calling functions
# Inherited from Person → "Hello, my name is Chimdiya."
print(student1.greet())
# New method in Student → "Chimdiya is studying Medicine."
print(student1.study())
print(student1.walk())    # Overridden method → "I am walking to class."
