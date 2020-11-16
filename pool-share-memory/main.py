from multiprocessing import Pool
from typing import Dict
import time


def sleep(name):
    print(global_cache)
    if name not in global_cache:
        print("not in")
        global_cache[name] = name
        time.sleep(3)
    print(name)
    return name


def init_global_cache(cache: Dict[str, str]) -> None:
    global global_cache
    global_cache = cache


cache = {}
list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
with Pool(processes=3, initializer=init_global_cache, initargs=(cache,)) as p:
    r = p.map(func=sleep, iterable=list)
    print(r)
