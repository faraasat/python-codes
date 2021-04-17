# list comprehension
ls = [i for i in range(100) if i%3==0]
print(ls)

# Dictionary Comprehension
dict = {i:f"item {i}" for i in range(100) if i%2==0}
print(dict)
dict1 = {value:key for key, value in dict.items()}  # dictionary reversed
print(dict1)

# Set Comprehension
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2",
                               "dress1", "dress2"]}
print(dresses)
print(type(dresses))

# Generator Comprehension
evens = (i for i in range(100) if i%2==0)
for items in evens:
    print(items, end=" ")
print("\n", type(evens))
