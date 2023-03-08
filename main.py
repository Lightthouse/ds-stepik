import numpy as np
import pandas as pd
from pprint import pprint
import random

# print(random.seed(10))

import scipy.stats as st
import math


x_men_bar = 45
sd_men = 9

x_w_bar = 34
sd_w = 10

n = 100
alpha = 0.95

se = math.sqrt(sd_men**2 / n + sd_w**2 / n)
t = (x_men_bar - x_w_bar) / se

df = n + n - 2

p_value = np.abs(st.t.ppf((1 - alpha) / 2, df))

print(f"""t-value: {t}
p-value for the {alpha * 100}% confidence interval: {p_value}
""")
if t > p_value:
    print("rejecting the null hypothesis")
elif t < p_value:
    print("acepting the null hypothesis")

    from scipy import stats

    ...

from scipy import stats
...
print(stats.f.sf(3.5, 3, 15))