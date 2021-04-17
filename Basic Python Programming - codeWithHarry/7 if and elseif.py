var1 = 6
var2 = 64
print("Enter num:\t")
var3 = int(input())

if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else :
    print("Lesser")

list1 = [5, 7, 2, 8]
print(2 in list1)
print(5 not in list1)
if 2 in list1:
    print("5 is in list")
else:
    print("5 is in not list")
if 15 not in list1:
    print("15 is not list")
else:
    print("15 is in list")