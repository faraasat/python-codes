# --------------------------- MAP --------------------------------
numbers = ["3", "34", "64"]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# map applies a function to whole list
numbers = list(map(int, numbers))
# here map is an object therefore we have typecasted it into list

numbers[2] = numbers[2] + 1
print(numbers[2])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
num = [2, 3, 5, 6, 76, 3, 3, 2]
square = list(map(lambda x:x*x, num))
print(square)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

# ----------------------------------- FILTER -----------------------
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_greater_5(num):
    return num > 5
"""
    Filter return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
"""
grt_than_5 = list(filter(is_greater_5, list1))
print(grt_than_5)

# ----------------------------------- REDUCE -----------------------
from functools import reduce
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numb = reduce(lambda x,y:x+y, list2)
print(numb)