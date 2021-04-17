def dec1(func):
    def nowexec():
        print("Executing now")
        func()
        print("Executed")
    return nowexec

@dec1   # it is a decorator
def who_is_harry():
    print("Harry is a good boy")

who_is_harry()
