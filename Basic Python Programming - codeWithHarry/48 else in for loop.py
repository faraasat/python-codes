khana = ["Roti", "Sabzi", "Chawal"]

for item in khana:
    if item == "Roti":
        print("Since value has found so else will not run because condition will break")
        break
else:
    print("Item not found")

for item in khana:
    if item == "Paratha":
        # this statement will not run because value not found and else will run
        break
else:
    print("Item not found")
