"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""

# it is a generator and used to save name
def gen(n):
    for i in range(n):
        yield i  # generate values on fly

g = gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())

h = "harry"
for c in h:
    print(c)

ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
