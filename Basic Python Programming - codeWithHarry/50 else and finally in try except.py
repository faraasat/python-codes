f1 = open("myFile.txt")

try:
    f = open("myFile1.txt")

except Exception as e:  # if except runs else will not run and vice versa
    print(e)

except EOFError as e:
    print(e)

except IOError as e:
    print(e)

else:
    print("Exception is not running")

finally:
    print("Run this any way")
    f1.close()

print("Important stuff........")
