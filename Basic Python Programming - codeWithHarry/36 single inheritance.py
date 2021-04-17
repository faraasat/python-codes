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

class Programmer (Employee):
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printProg(self):
        return f"Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role} and languages are {self.languages}"

harry = Employee("Harry", 455, "Instructor")
Rohan = Employee.from_dash("Karan-480-Student")

shubam = Programmer("Shubam", 555, "Programmer", ["Python"])
Karan = Programmer("Karan", 699, "Programmer", ["Python, Cpp"])
print(Karan.printProg())
