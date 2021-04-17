# == => value equality  -----> two objects have same value
# is => reference equality  -----> two references refers to the same object

a = [0, 3, 5]
b = a
print("a == b => ", a == b)
print("a is b => ", a is b)
c = b[:]
print("b == c => ", b == c)
print("b == c => ", b is c)
