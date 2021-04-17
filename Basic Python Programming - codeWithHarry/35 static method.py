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

    @classmethod
    def from_dash(cls, string):  # here it is working as alternative constructor
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)

harry = Employee("Harry", 455, "Instructor")
karan = Employee.from_dash("Karan-480-Student")

print(karan.printdetails())

karan.printGood("harry")