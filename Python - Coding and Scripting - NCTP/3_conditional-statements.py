cars = ["audi", "bmw", "suzuki", "toyota", "honda"]

isCarFound = False

for car in cars:
    if car == "toyota":
        isCarFound = True

if isCarFound == True:
    print("Toyota is present in this list")
else:
    print("No this brand is not toyota")

myCar = "bmw"
print(myCar == "bmw")

print(myCar.lower())

if (True) and (False):
    print("True for and")
elif (True) or (False):
    print("True for or")
elif not (True):
    print("True for not")
else:
    print("True for none")


statement = "Hello! have a great day today"
if 'great' in statement:
    print("In statement")
else:
    print("Not in statement")
