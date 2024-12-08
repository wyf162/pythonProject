# _*_ coding: utf-8 _*_
# @Time : 2023/01/07 8:10 PM
# @Author : yefe
# @File : interview_yefei.wang

import numpy as np
import time


def shift(arr: np.array, n: int) -> np.array:
    return np.concatenate((np.full(n, arr[0]), arr[:-n]))


def simple_feature(arr: np.array) -> np.array:
    threshold = -1e-13
    x1 = shift(arr, 30)
    x2 = shift(arr, 15)
    x = x1 - x2
    y = shift(arr, 15)
    z = x - y
    i1 = z < threshold
    i1 = i1 * 1

    i0 = z >= threshold
    i0 = i0 * 1
    t = shift(arr, 1) - arr
    t = t*i0

    return t+i1


if __name__ == '__main__':
    np.random.seed(1)
    length = 200000
    tic = time.time()
    A = np.random.random(length).astype(np.float64)
    toc = time.time()
    print(f"Data generation time: {(toc - tic) * 1e3} ms.")

    shift_win = 3
    tic = time.time()
    B = shift(A, 3)
    toc = time.time()
    print(f"Computing time: {(toc-tic)*1e3} ms.")

    tic = time.time()
    C = simple_feature(A)
    toc = time.time()
    print(f"Computing time: {(toc - tic) * 1e3} ms.")
