# -*- coding: utf-8 -*-
# @Time: 2024/6/28 10:24
# @Author: yfwang
# @File: D2.py
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py
def z_function(S):
    """
    Z Algorithm in O(n)
    :param S: text string to process
    :return: the Z array, where Z[i] = length of the longest common prefix of S[i:] and S
    """

    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z


for _ in range(int(input())):
    s = input()
    n = len(s)
    if n % 2 == 1:
        print(0)
        continue
    Zf = z_function(s)
    Zb = z_function(s[::-1])[::-1]
    ans = 0
    for i in range(n // 2 + 1):
        if Zf[i] >= i and Zb[i + n // 2 - 1] >= n // 2 - i: ans += 1
    print(ans)