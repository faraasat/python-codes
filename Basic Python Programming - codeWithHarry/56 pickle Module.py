import pickle

# Pickling a python project
# cars = ["Audi", "BMW", "Maruti", "Tuzuki"]
# file = "myCar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

"""
We do pickle because when we open a binary file it do not open correctly that is why we use it 
"""

file = "myCar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))