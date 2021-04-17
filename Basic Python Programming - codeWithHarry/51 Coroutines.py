# it means we first run the function half and then when every time we run it, it start from half
import time

def searcher():
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in book")
        else:
            print("Your text is not in book")

search = searcher()
print("--------------Search started--------------")
next(search)  # next method will run function till while
print("--------------Next method run--------------")
search.send("harry")
input("Press any key to continue: ")
search.send("good")
input("Press any key to continue: ")
search.send("boy ")
input("Press any key to continue: ")
search.send("hello")
input("Press any key to continue: ")
search.send("book")
search.close()  # to stop coroutine
search.send("Hello")