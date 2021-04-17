class Employee:
    no_of_leaves = 8
    var = 8
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
        return f"Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}" \
               f" and languages are {self.languages}"

class Player:
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

class CoolProgrammer(Employee, Player):  # order of parent classes is important
    language = "C++"
    def printLang(self):
        print(self.language)


harry = Employee("Harry", 455, "Instructor")
Rohan = Employee.from_dash("Rohan-480-Student")
Karan1 = Programmer("Karan", 699, "Programmer", ["Python, Cpp"])
shubam = Player("Shubam", ["Cricket"])
Karan = CoolProgrammer("Karan", 8999, "CoolProgrammer")
det = Karan.printdetails()
print(det, "and Var is =>", Karan.var)
