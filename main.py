import numpy as np
import pandas as pd
from pprint import pprint

num = int(input())


def fib(n):
    res = [0, 1]
    if n < 3:
        return res[0:n]

    counter = 2
    while counter < n:
        numb = res[-1] + res[-2]
        res.append(numb)
        counter += 1

    print(*res)

fib(num)