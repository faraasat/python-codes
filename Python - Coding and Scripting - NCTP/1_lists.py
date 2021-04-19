grocery = ['eggs', 'bread', 'vegetables']
print(grocery)
print(grocery[2].title())

tmp = "I want to eat {} and {}".format(grocery[2].upper(), grocery[0].lower())
print(tmp)

grocery.append('oil')
print(grocery)

grocery.insert(0, 'butter')
print(grocery)

del grocery[0]
print(grocery)

item_to_purchase = grocery.pop()
print(item_to_purchase)
print(grocery)

item_to_purchase = grocery.pop(1)
print(item_to_purchase)
print(grocery)

grocery.remove('eggs')
print(grocery)

grocery.append('marshmellow')
grocery.append('fruit')
grocery.append('jelly')
grocery.append('tea')
grocery.append('coffee')
print(grocery)

grocery.sort()
print(grocery)

grocery.reverse()
print(grocery)

sorted_array = sorted(grocery)   # it does not change real array
print(sorted_array)

length_of_grocery = len(grocery)
print(length_of_grocery)
