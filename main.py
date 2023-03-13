import numpy as np
import pandas as pd
from pprint import pprint
import math


def evq(base, dep):
    evq_result = []
    for vector in base:
        evq_result.append(math.sqrt(sum((vector[ind] - val) ** 2 for ind, val in enumerate(dep))))

    return evq_result


def man(base, dep):
    man_result = []
    for vector in base:
        man_result.append(sum(abs(vector[ind] - val) for ind, val in enumerate(dep)))

    return man_result


def max_r(base, dep):
    max_result = []
    for vector in base:
        max_result.append(max([abs(vector[ind] - val) for ind, val in enumerate(dep)]))

    return max_result


def normalize(matrix):
    norm_res = []
    for row in matrix:
        mx = max(row)
        mn = min(row)
        md = mx - mn
        norm_row = [(val - mn) / md for val in row]
        norm_res.append(norm_row)

    return norm_res


def predict_man(matrix, search_vector):
    search_column = [row[-1] for row in matrix]
    man_values = man(matrix, search_vector[:-1])
    upside_down_man_values = [1 / i for i in man_values]
    koef = 1 / sum(upside_down_man_values)
    search_column_by_length = [val * upside_down_man_values[ind] for ind, val in enumerate(search_column)]
    return koef * sum(search_column_by_length)


a = [-1, 0]
b = [1, 2]
c = [2, -2]
d = [-3, -1]
e = [3, 2]

q1 = [0, 0]


# print(evq([a, b, c, d, e], q1))
# print(man([a, b, c, d, e], q2))

import sympy
w1, w0 = sympy.symbols('w1 w0')
y = sympy.simplify((1 - 2*w1 + w0)**2 +
                   (1 - w1 + w0)**2 +
                    (1-w0)**2+
                   (1 - w1 - w0)**2 +
                   (1 - 2*w1 - w0)**2)
y1 = sympy.diff(y, w0)
y2 = sympy.diff(y, w1)

print(y1)
print(y2)


# P(A) = 0,70, P(B) = 0,30
# P(1|A) = 0,10, P(1|B) = 0,50
# P(A|1) - ?
# P(A|1) = P(1|A) * P(A) / P(1)
# P(1) = P(1|A) * P(A) + P(1|B) * P(B)
# P(1) = 0,10 * 0,70 + 0,50 * 0,30 = 0,22
# P(A|1) = 0.1 * 0.7 / 0.22