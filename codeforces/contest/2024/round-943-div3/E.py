# -*- coding : utf-8 -*-
# @Time: 2024/5/2 23:34
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    if n == 2:
        ans = [(1, 1), (2, 2)]
    else:
        ans = [(1, 1), (2, 1), (3, 3)]
        for x in range(4, n + 1):
            ans.append((x, x))
    for i in range(n):
        print(*ans[i])
    # print(ans)
    # st = set()
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         dis = abs(ans[i][0] - ans[j][0]) + abs(ans[i][1] - ans[j][1])
    #         st.add(dis)
    # print(list(sorted(st)))
