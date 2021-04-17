i = 0
while i < 45:
    print(i+1, end=" ")
    i = i + 1
print()
i = 0
while True:  # while 1 is also same
    i = i + 1
    if i+1 < 5:
        continue

    print(i+1, end=" ")

    if i == 44:
        break

