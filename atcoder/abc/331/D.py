# -*- coding : utf-8 -*-
# @Time: 2023/12/2 20:16
# @Author: yefei.wang
# @File: D.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N, Q = MI()
grid = [input() for _ in range(N)]

pre_sum = [[0 for j in range(N + 1)] for i in range(N + 1)]
for i in range(N):
    for j in range(N):
        pre_sum[i + 1][j + 1] = pre_sum[i][j + 1] + pre_sum[i + 1][j] - pre_sum[i][j] + int(grid[i][j] == 'B')

# for i in range(N + 1):
#     print(*pre_sum[i])
# print()


def get_b(X, Y):
    k1, k2 = X // N, Y // N
    x, y = X % N, Y % N
    cnt1 = k1 * k2 * pre_sum[N][N]
    cnt2 = k2 * pre_sum[x][N]
    cnt3 = k1 * pre_sum[N][y]
    cnt4 = pre_sum[x][y]
    cnt = cnt1 + cnt2 + cnt3 + cnt4
    return cnt


for _ in range(Q):
    A, B, C, D = MI()
    h, w = C - A + 1, D - B + 1
    c1 = get_b(A, B)
    c2 = get_b(A, B + w)
    c3 = get_b(A + h, B)
    c4 = get_b(A + h, B + w)
    # print(c1, c2, c3, c4)
    ans = c4 + c1 - c2 - c3
    print(ans)
