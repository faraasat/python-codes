# Dictionary is nothing but key value pairs
d1 = {}
print("Type of d1 =>", type(d1))

d2 = {"Harry":"Burger", "Rohan":"Fish", "SkillF":"Roti", "Shubam":{"B":"maggie", "L":"roti", "D":"Chicken"}}  # Shubam has a dictionary in dictionary

print("d2 =>", d2)
print("d2['Harry'] =>", d2["Harry"])
print("d2['Shubam'] =>", d2["Shubam"])
print("d2['Shubam']['B'] =>", d2["Shubam"]["B"])

# To add any item to dictionary
d2["Ankit"] = "Junk Food"
print("d2['Ankit'] = 'Junk Food' =>", d2)
d2[420] = "Kebab"
print("d2[420] = 'Kebab' =>", d2)

# To delete an item from dictionary
del d2[420]
print("Deleted =>", d2)

# For copying. If we do not copy the d2 will also be modified by modifying d3
d3 = d2.copy()
print("d3 =>", d3)

# To get the value of item
print("d2.get('Harry') =>", d2.get("Harry"))

# To add another item
d2.update({"Leena":"Toffee"})
print("d2.update({'Leena':'Toffee'}) =>", d2)

# To display keys and items
print("d2.keys() =>", d2.keys())
print("d2.items() =>", d2.items())
print("d2.value() =>", d2.values())

# To check that a key is in dictionary or not
print("Rohan" in d2)