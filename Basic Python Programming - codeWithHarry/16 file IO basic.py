# File IO Basics

"""
"r" - Open file for reading - default
"w" - Open file for writing
"x" - Creates a file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""

# f = open("myFile.txt", "rt")  # rt mode is default
# print(f.readline())
# print(f.readlines())
# content = f.read()
# for line in f:
#     print(line, end=" ")
# print(content)
# content = f.read(3)   --> only read three characters
# print(content)
# f.close()

# f = open("myFile1.txt", "a")  # "w" deletes content and then re-write its content
# a = f.write("Harry is very good\n")
# print(a)
# f.close()

# f = open("myFile1.txt", "r+")  # read and write both
# print(f.read())
# f.write("Thank you\n")
# f.close()

# f = open("myFile1.txt")
# print(f.tell())  # tells where is file pointer
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.tell())  # tells where is file pointer
# f.seek(9)  # reset the file pointer
# print(f.tell())
# print(f.readline(), end="")
# f.close()

"""
    In this we use w for write mode and if the file does not exist then it will create 
    the file and write in it.
    In this we use r for read mode and if the file does not exist then it will throw
    file not find error.
    In this we use a for append mode.
    with open("myFile.txt", "mode") as file
"""
# with open("myFile1.txt") as f:  #it is same as f = open() and also doesnot require f.close
#     a = f.read(4)
#     print(a)

# with open("myNewFile.txt", "w+") as f:
#     f.write("This file doesnot exist")
#     f.seek(0)
#     print(f.read())

with open("myNewFile.txt", "r+") as f:  # this do not create file if not available
    f.write("This file doesnot exist")
    f.write("This file doesnot exist")
    f.write("This file doesnot exist")
    f.seek(0)
    print(f.read())