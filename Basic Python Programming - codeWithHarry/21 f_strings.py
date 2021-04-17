import math
# This is not f_string, it is only string formatting
me = "Harry"
a1 = 1
a = "This is %s %s" %(me, a1)
print(a)
# This also string formatting
a = "This is {1} {0}"
b = a.format(me, a1)
print(b)
# f string => fast string
a = f"this is {me} {a1} {math.sin(65)}"
print(a)