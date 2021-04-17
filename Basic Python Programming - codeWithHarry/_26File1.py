def printhar(String):
    return f"Give me this string {String}"

def add(num1, num2):
    return num1 + num2 + 5

print("And the main is ", __name__)

if __name__ == '__main__':  # same as main function in c++ or java
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)