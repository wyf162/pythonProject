# -*- coding : utf-8 -*-
# @Time: 2022/7/10 14:28
# @Author: yefei.wang
# @File: 6115_ideal_arrays.py

from typing import List

MX_K = 13
MX = 10**4+1
MOD = 10**9+7


def f(x: int) -> List[int]:
    ks = []
    p = 2
    while p * p <= x:
        if x % p == 0:
            k = 0
            while x % p == 0:
                k += 1
                x //= p
            ks.append(k)
        if x > 1:
            ks.append(1)
    return ks


ks = [f(x) for x in range(MX)]

