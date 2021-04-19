import time

grocery = ['eggs', 'bread', 'vegetables', 'marshmellow', 'fruit', 'jelly']

iterator = 1
for item in grocery:
    statement = f"{iterator}. {item}"
    print(statement)
    iterator += 1

for index in range(0, 2):
    print(index)

for index in range(0, 7, 3):
    print(index)
    time.sleep(1)
