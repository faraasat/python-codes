"""Faulty Calculator"""

num1 = int(input("Enter num1:\t"))
num2 = int(input("Enter num2:\t"))
opera = input("Enter any of: + - * / %\t")

if num1 == 58 and num2 == 9 and opera == '+':
    print("77")
elif num1 == 64 and num2 == 6 and opera == '/':
    print("4")
else:
    print("good!")