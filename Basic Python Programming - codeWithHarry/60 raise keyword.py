# a = input("What is your name: ")
# b = input("How much do you earn: ")
#
# if int(b)==0:
#     raise ZeroDivisionError("B is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")

c = input("Enter your name: ")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked. He is not allowed")

    print("Exception handled")