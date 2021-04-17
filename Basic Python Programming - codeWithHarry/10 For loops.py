list1 = [["Harry", 2], ["Larry", 5], ["Carry", 6], ["Marry", 10]]
for item, lollipop in list1:
    print(item, "and Lolly is: ", lollipop)

# We typecasted list into dictionary
dict1 = dict(list1)
print(dict1)
for item, lollipop in dict1.items():
    print(item, "and Lolly is: ", lollipop)

list2 = ["asd", 1, 5, "adf", "wsd", 67, "ad", 35, "adaad", "aer", 67]
for num in list2:
    if str(num).isnumeric() and num > 6:
        print(num, end="\t")
print()

for num in range(5):  # it will start from 0 and ends on 4
    print(num, ": Nasir", end="\t")
print()

for num in range(1, 10):  # it will start from 1 and ends on 9. Since, 10-1 = 9
    print(num, end="\t")
print()

for num in range(1, 10, 2):  # it will start from 1 and ends on 9 and will take two steps
    print(num, end="\t")
print()

cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta", "Multan"]
for city in cities:
    print(city, end="\t")
print()

country = "Pakistan"
for char in country:
    print(char, end=" ")
print()