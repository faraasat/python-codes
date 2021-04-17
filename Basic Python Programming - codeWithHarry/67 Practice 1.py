yearAge = int(input("What is your Age/Year of birth "))

isAge = False
isYear = False
if yearAge < 125:
    isAge =True
elif yearAge > 1900:
    isYear = True
if yearAge < 1900:
    print("You seem to be oldest person to alive")
    exit()
if yearAge > 2020:
    print("You are not born yet")
    exit()
else:
    print("There was some problem with your age/year of birth")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

