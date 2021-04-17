class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set is using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


asia_supporter = Employee("Asia", "Supporter")
print(asia_supporter.explain())

asia_supporter.fname = "Africa"
print(asia_supporter.email)  # we donot use () in this because it is a property

asia_supporter.email = "this.that@codewithharry.com"
print(asia_supporter.email)
print(asia_supporter.fname)
print(asia_supporter.lname)

del asia_supporter.email
print(asia_supporter.email)

asia_supporter.email = "Harry.Perry@codewithharry.com"
print(asia_supporter.email)