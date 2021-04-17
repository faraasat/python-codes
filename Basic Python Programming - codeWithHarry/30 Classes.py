class Student:
    pass   # pass means nothing

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["Physics", "Maths"]
print(harry.name, larry.subjects)
