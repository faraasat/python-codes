class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee("Harry", 455, "Instructor")
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 444
# rohan.role = "Student"

print(harry.printdetails())