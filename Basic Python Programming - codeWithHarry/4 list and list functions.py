grocery = ["Harpic", "Vim Bar", "Deoddrant", "Bhindi", "Lollypop", 56]
print(grocery)

myNumbers = [2, 7, 8, 11, 3]

myNumbers.sort()  # for sorting they effect original list
print("myNumbers after sort() =>", myNumbers)
myNumbers.reverse()  # to reverse they effect original list
print("myNumbers after reverse() =>", myNumbers)

print("myNumbers after [:4] =>", myNumbers[:4])  # slice out the 4th element from last
print("myNumbers after [::2] =>", myNumbers[::2])  # it means skip 1 element from the list
print("myNumbers after [::-1] =>", myNumbers[::-1])

print("myNumbers length =>", len(myNumbers))
print("myNumbers after min() =>", min(myNumbers))
print("myNumbers after max() =>", max(myNumbers))

myNumbers.append(10)  # appends a value at the end of the list
print("myNumbers after append =>", myNumbers)
myNumbers.insert(2, 7)  # it appends at our req position (index, number)
print("myNumbers after insert =>", myNumbers)
myNumbers.extend([22, 34, 56, 90])  # To append more than one values
print("myNumbers after extend =>", myNumbers)

print("myNumbers after count =>", myNumbers.count(3))  # counts the number of occurance of an element
print("myNumbers after index() =>", myNumbers.index(7))  # return the first index of an element

myNumbers.remove(11)  # removes the given value
print("myNumbers after remove =>", myNumbers)
del myNumbers[2]  # removes the value on given index
print("myNumbers after del =>", myNumbers)
print(myNumbers.pop())  # remove last element from list and also return the same element
print("myNumbers after pop =>", myNumbers)
print(myNumbers.pop(3))  # remove given index of element from list and also return the same element
print("myNumbers after pop(3) =>", myNumbers)

myNumbers[1] = 98  # To replace a number
print("myNumbers after myNumber[1] = 98 =>", myNumbers)

myNumbers2 = myNumbers.copy()  # Copy the list
print("myNumbers2 =>", myNumbers2)
myNumbers2.clear()  # clears all the list
print("myNumbers2 =>", myNumbers2)

# Mutable - can change
# Immutable - cannot
# We can slice or use values from tuple but cannot change, delete or append them
tp = (1, 2, 3)
print(tp)  # tp is touple and it is immutable
pt = (1,)  # with one number , is also neccessary
print(pt)
abc = 12, 15, 18  # also a tuple
print(abc)

a = 1
b = 2
a, b = b, a   # to swap numbers
print(a, b)
