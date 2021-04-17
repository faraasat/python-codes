# l = 10  # Global variable
#
# def function1(n):
#     # l = 5
#     m = 8
#     global l  # to change value of global variable
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# print(l)

def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)