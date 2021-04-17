class Employee:
    no_of_leaves = 8
    var = 6             # public variable
    _protect = 8        # protected variable
    __private = 98      # private variable

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

emp = Employee("Harry", 343, "Programmer")
print(emp._protect)  # to access protected variable we use _ before variable name
print(emp._Employee__private)  # this is called name angling and it is used to access private variable

