myStr = "Harry is a good boy!"
print(len(myStr))
print(myStr[0:19])  # in 0:19 0 is including and 19 is excluding
print(myStr[0:5:2])  # :2 means skip one character
print(myStr[:5])
print(myStr[0:])
print(myStr[::])
print(myStr[::2])
print(myStr[-4:-1])  # count and slice from the last element of String
print(myStr[::-1])  # Reverses the string
print(myStr[::-2])  # reverse string with skipping 1 element of String
print(myStr[::-3])

print(myStr.isalnum())  # If we delete the spaces of string isalnum() will return true
print(myStr.isalpha())

print(myStr.capitalize())  # Capatilize first word
print(myStr.lower())  # Convert into lowercase
print(myStr.upper())  # Convert into uppercase
print(myStr.title())  # Convert into a Title

print(myStr.endswith("boy!"))  # Return boolean value
print(myStr.find("is"))  # Return index of given word
print(myStr.replace("is", "are"))  # replaces with given value
print(myStr.count("o"))
