# -*- coding : utf-8 -*-
# @Time: 2023/11/4 11:17
# @Author: yefei.wang
# @File: C.py
import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    N, M, K = MI()
    if K == 1:
        print(M)
    elif K == 2:
        print(N % 2)
    elif K == 3:
        if N > M:
            if (N + M * 2) % 3 == 0:
                print(0)
            else:
                print(1)
        else:
            print(M - N)
    elif K % 2:
        x, y = divmod(N + M * 2, K)
        if N <= x:
            rst = M - N * (K // 2)
        else:
            rst = (y + 1) // 2
        print(rst)
    else:
        x, y = divmod(N + M * 2, K)
        if y <= 2 * M:
            rst = (y + 1) // 2
        else:
            rst = (y - 2 * M) + M
        print(rst)
