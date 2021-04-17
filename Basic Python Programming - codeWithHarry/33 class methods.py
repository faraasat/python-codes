class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod  # class method can only access class variables
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 355, "Student")

harry.change_leaves(34)  # it will change class variable rather than object variable

print(harry.printdetails())
print(Employee.no_of_leaves)