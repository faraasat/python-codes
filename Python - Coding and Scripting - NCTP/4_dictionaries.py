dic = {"name": "Ali", "email": "ali@gmail.com"}

print(dic["name"])
print(dic["email"])

name_input = "Ahmed"
email_input = "ahmed@gmail.com"

dic["name"] = name_input
dic["email"] = email_input

print(dic["name"])
print(dic["email"])

myList = [{"name": "ahmed", "email": "ahmed@gmail.com"},
          {"name": "ali", "email": "ali@gmail.com"}]
print(myList)

for temp_dic in myList:
    print(temp_dic["name"] + " " + temp_dic["email"] + " ")

print(myList[0]["name"])

myDatabase = {
    '1': [
        {"name": "ahmed", "email": "ahmed@gmail.com"},
        {"work": "44th Bahria Town", "phone": "1123213213"}
    ],
    '2': [
        {"name": "ali", "email": "ali@gmail.com"},
        {"work": "44th Bahria Town", "phone": "1123213213"}
    ]
}

print(myDatabase['2'][1]["work"])
