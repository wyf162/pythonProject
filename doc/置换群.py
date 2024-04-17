# -*- coding: utf-8 -*-
# @Time: 2024/4/17 15:24
# @Author: yfwang
# @File: 置换群.py
import itertools
import typing


class FenwickTree:
    """
    Reference: https://en.wikipedia.org/wiki/Fenwick_tree
    https://github.com/atcoder/ac-library/blob/master/document_en/fenwicktree.md
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


def compute_inv(nums):
    n = len(nums)
    xi = [(x, i) for i, x in enumerate(nums)]
    xi.sort(reverse=True)
    fen = FenwickTree(n)
    cnt_inv = 0
    for x, i in xi:
        cnt_inv += fen.sum(0, i)
        fen.add(i, 1)
    return cnt_inv


def construct(n, cnt_inv):
    B = []

    x = n - 1
    while cnt_inv >= 0 and x >= 0:
        if cnt_inv >= x:
            B.append(x)
            cnt_inv -= x
            x -= 1
        else:
            for i in range(x - cnt_inv):
                B.append(i)
            B.append(x)
            for i in range(x - cnt_inv, x):
                B.append(i)
            cnt_inv = -1

    return B


def transform(A, B):
    # B[i] = P[A[i]]
    n = len(A)
    ind = [0] * n
    for i, x in enumerate(B):
        ind[x] = i

    P = [0] * n
    for i, x in enumerate(A):
        P[ind[x]] = i
    return P


if __name__ == '__main__':
    A = [0, 1, 2, 3]
    P = [0, 3, 2, 1]
    B = [0] * len(A)
    for i in range(len(A)):
        B[i] = P[A[i]]
    print(B)

    # for B in itertools.permutations(A):
    #     # print(B)
    #     B = list(B)
    #     P = transform(A, B)
    #     BB = [0] * len(B)
    #     for i in range(len(B)):
    #         BB[i] = P[A[i]]
    #     if B != BB:
    #         print(False)
    #         print(B)
    #         print(BB)

    # n = 4
    # cnt = 5
    # nums = construct(n, cnt)
    # cc_inv = compute_inv(nums)
    # print(nums)
    # print(cc_inv)
