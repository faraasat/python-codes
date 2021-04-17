import time

initial = time.time()
k=0
while(k<45):
    print("This is Harry bhai")
    k+=1
print("While loop ran in ", time.time()-initial, "Seconds\n")

initial2 = time.time()
print(initial)
for i in range(45):
    print("This is Harry bhai")
print("For loop ran in ", time.time()-initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

time.sleep(1)  # sleep for 1 second

print("Hello after time.sleep()")
