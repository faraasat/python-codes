import time
from functools import lru_cache

@lru_cache(maxsize=3)  # it means it will only store recent three calls
def some_work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("some_work(3) done")
    some_work(1)
    print("some_work(1) done")
    some_work(2)
    print("some_work(2) done")
    some_work(5)
    print("some_work(5) done")
    some_work(3)  # this will also take time because we have given limit of 3 functions to cache
    print("some_work(3) done")
    some_work(5)  # since it is within 3 therefore it will not take time
    print("some_work(5) done")