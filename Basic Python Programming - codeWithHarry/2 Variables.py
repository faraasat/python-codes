#Variables
var1 = "Hello World! "
var2 = 4
var3 = 30.7
var4 = "Potter"
print(var1)
print(var2)
print(var3)
print(var4)
print(type(var1))
print(type(var2))
print(type(var3))
print(var3 + var2)
print(var1 + var4)

#type casting
"""
str()  float()  int()
"""
var5 = "36"
var6 = "34"
print(int(var5))
print(type(int(var5)))
print(var5 + var6)
print(10 * int(var5) + int(var6))
print(10 * str(int(var5) + int(var6)))

#to print a line n times from print
print(5 * "Hello World\n")

#to make user input
print("Enter You number")
inputNum = input()
"""here we cannot add anything b/c input give all values as string"""
print("Your input is: ", inputNum)
print("Your input is: ", int(inputNum) + 10)

# Another way to take input:
inp = input("\nEnter num:\t")
print(inp)