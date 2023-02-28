import numpy as np
from pprint import pprint

def multik():
    a = [
        [11, 22, 33],
        [44, 55, 66],
        [66, 88, 99],
    ]

    b = [
        [1, 2, 3],
        [4, 5, 6],
        [6, 8, 9],
    ]

    f_r = 1 * 11 + 4 * 22 + 6 * 33
    s_r = 2 * 11 + 5 * 22 + 8 * 33


    def custom_mult(f_arr, s_arr):
        result = []
        columns = list(map(lambda *args: args, *s_arr))

        def scalar_mult(*args):
            mult_values = []
            for col in columns:
                current_sum = sum(col_val * row_val for col_val, row_val in zip(col, *args))
                mult_values.append(current_sum)

            return mult_values

        for row in f_arr:
            current_res = scalar_mult(row)
            result.append(current_res)

        return result


    def numpy_mult(f_arr, s_arr):
        na = np.array(f_arr)
        nb = np.array(s_arr)
        return np.dot(na, nb)


    np_res = numpy_mult(a, b)
    custom_res = custom_mult(a, b)
    pprint(np_res == custom_res)


# ===========
def scalar():
    a = np.random.sample((1, 3))
    a = list(a)[0]
    b = np.random.sample((1, 3))
    b = list(b)[0]
    print(a, b)

    def no_numpy_scalar(v1, v2):
        #param v1, v2: lists of 3 ints
        #YOUR CODE: please do not use numpy
        return sum(v1_value * v2_value for v1_value, v2_value in zip(v1,v2))


    def numpy_scalar (v1, v2):
        return np.dot(v1,v2)

    print(no_numpy_scalar(a, b))
    print(numpy_scalar(a, b))

#==============================
def diag_2k(a):
    #param a: np.array[size, size]

    dig = a.diagonal()
    return dig[dig % 2 == 0].sum(initial=0)


# ==============================
def transform_rows():
    def transform_clever(X, a=1):
        Y = np.copy(X)
        Y[:, 1::2] = a
        Y[:, 0::2] **= 3
        return np.hstack((X, Y[:, ::-1]))

    def transform(X, a=1):
        """
        param X: np.array[batch_size, n]
        """
        res = np.hstack((X, X))

        def ft(art):
            change_part = art.size // 2
            art[change_part::2] **= 3
            art[change_part + 1::2] = a
            art[:change_part - 1:-1] = art[change_part::]

        np.apply_along_axis(ft, 1, res)

        return res

    inp_art = np.array([[100, 200, 300, 400, 500], [100, 200, 300, 400, 500]])

    print(transform(inp_art))


#  ==============================
def encode_task():
    def encode(a):
        # YOUR CODE

        inner_arr = np.append(a, -1)
        prev_val = 1
        val_count = inner_arr[0]
        res_values = np.array([], dtype=np.int32)
        res_counts = np.array([], dtype=np.int32)
        for i in inner_arr[1::]:

            if not prev_val == i:
                res_values = np.append(res_values, prev_val)
                res_counts = np.append(res_counts, val_count)
                val_count = 1

            else:
                val_count += 1

            prev_val = i

        return res_values, res_counts

    def encode_clever(a):
        is_new_in_row = np.array(a[1:] != a[:-1])
        position = np.append(np.where(is_new_in_row), len(a) - 1)
        lengths = np.diff(np.append(-1, position))
        return (a[position], lengths)

    def encode_clever2(a):
        oper = np.asarray(a)  # создаём копию исходного массива, например [1 2 2 2 2 3 3 3 3 1 2 2 2 1 1]
        size = np.size(oper)  # size в роли size

        # oper[1:] массив с первого, а не нулевого элемента [2 2 2 2 3 3 3 3 1 2 2 2 1 1]
        # oper[:-1] массив без последнего элемента [1 2 2 2 2 3 3 3 3 1 2 2 2 1]
        # oper[1:] != oper[:-1] получаем массив bool (True/False), где True отмечает позицию смены элемента серии
        #   [ True False False False  True False False False  True  True False False True False]
        # np.where(oper[1:] != oper[:-1]) создаёт массив индексов где заканчивается одна серия и начинается новая
        # другими словами это индексы последнего элемента в каждой серии повторов
        #   [ 0  4  8  9 12]
        # для корректной обработки последней серии добавим индекс последнего элемента последней серии
        #   [0  4  8  9 12 14]
        pos = np.append(np.where(oper[1:] != oper[:-1]), size - 1)

        # создадим массив содержащий по одному элементу каждой серии в правильной последовательности
        #   [1 2 3 1 2 1]
        el_arr = oper[pos]

        # np.diff() создаёт массив разниц между парами элементов в массиве
        # добавим в начало массива позиций -1 для коректоной обработки первой серии, так как её длину неоткуда считать
        # получаем массив длинн каждой серии
        #   [1 4 4 1 3 2]
        ser_len = np.diff(np.append(-1, pos))

        return el_arr, ser_len

    def encode_clever23(a):
        # YOUR CODE
        idx_unique = np.hstack((0, 1 + np.where(a[:-1] != a[1:])[0], a.size))
        count = (idx_unique[1:] - idx_unique[:-1])

        return (a[idx_unique[:-1]], count)

    input_arr = np.array([1, 2, 1, 1, 2, 3, 3, 3, 0])
    input_arr2 = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])

    print(encode(input_arr2))
