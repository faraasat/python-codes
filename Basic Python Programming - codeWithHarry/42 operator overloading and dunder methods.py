import math

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

    def __add__(self, other):  # dunder method
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return math.floor(self.salary / other.salary)

    def __repr__(self):
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):  # this method is preferred than repr method
        return self.printdetails()

emp1 = Employee("Harry", 345, "Programmer")
emp2 = Employee("Rohan", 85, "Cleaner")
print(emp1 + emp2)
print(emp1 / emp2)
print(emp1 // emp2)
print(emp1)
print(repr(emp2))  # since str is preferred so to use repr we do like this
