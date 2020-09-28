from multiprocessing import Pool
import time


def sleep(name):
    time.sleep(3)
    print(name)
    return name


list = [1, 2, 3, 4, 5]
with Pool(processes=3) as p:
    r = p.map(func=sleep, iterable=list)
    print(r)
