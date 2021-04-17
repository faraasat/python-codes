import json

# # To write a file
# with open("$4jsonListFile.json", "w") as f:
#     json.dump([11, 22, 33, 44, 55], f)
#     json.dump([15, 30, 45, 60, 75], f)

# To read a file
with open("$4jsonListFile.json", "r") as f:
    content = json.load(f)
    print(content)

# # To append a file
# with open("$4jsonListFile.json", "a") as f:
#     json.dump([5, 10, 15, 20, 25], f)
#     json.dump([10, 20, 30, 40, 50], f)
#     json.dump([15, 30, 45, 60, 75], f)

# customer_29876 = {"first name": "David", "last name": "Elliot", "address" :
#                   "4803 Wellesley St."}
# with open("$4jsonDictFile.json", "w") as f:
#     json.dump(customer_29876, f)
#     json.dump(customer_29876, f)

# with open("$4jsonDictFile.json", "r") as f:
#     content = json.load(f)
#     print(content)
