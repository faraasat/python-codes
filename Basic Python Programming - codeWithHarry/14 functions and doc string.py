a = 9
b = 8
c = sum((a, b))
print(c)

def function1(a, b):
    print("Hello you are in function1", a + b)
function1(2, 3)

def function2(a, b):
    """THe first comment written in a function is called doc_string"""
    average = (a+b) / 2
    # print(average)
    return average
v = function2(10, 5)
print(v)
print(function2.__doc__)

def fullName(first, middle, last):
    print(first, middle, last)
fullName("Farasat", "Ali", "Azeemi")

"""Keyword parameters"""
fullName(middle="Ali", first="Farasat", last="Azeemi")  # these are called keyword arguments
fullName("Farasat", "Ali", last="Azeemi")  # keyword arguments are always at last

"""Default Parameters"""
def fullName(first, last, middle=""):  # default arguments must be at last
    print(first, middle, last)
fullName("Farasat", "Azeemi")

# here * allows us to give arbitrary number of arguments
def pizzaOrder(size, flavour, *toppings):
    print(f"Your order of pizza of size {size}, flavour "
          f"{flavour} and toppings is {toppings} is ready")
pizzaOrder(12, "Chicken Tikka", "Olives", "Mashrooms", "Extra Cheese")

# Function as variable
def sum(a, b):
    return a+b
def sub(a, b):
    return a-b
result = sum(3, 2) + sub(3, 2)
print(result)
