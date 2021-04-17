import os

print(dir(os))
print("pwd => ", os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("myFile.txt")
print("Files and folder in my project ", os.listdir())
print("Files and folder in C ", os.listdir("C://"))
# os.mkdir("this")  # to make folder
# os.rmdir("this")
# os.makedirs("this/that")  # to make folders and sub folders
# os.rename("this", "thised")
print(os.environ.get('path'))
print(os.path.join("C://", "harry.txt"))
print(os.path.exists("C://Program Files"))
print(os.path.isdir("C://Program Files"))
print(os.path.isfile("C://Program Files//Notepad++//notepad++.exe"))

