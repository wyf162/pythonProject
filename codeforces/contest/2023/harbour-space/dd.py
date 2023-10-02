# -*- coding : utf-8 -*-
# @Time: 2023/8/27 17:40
# @Author: yefei.wang
# @File: dd.py

import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main(t):
    n = int(input())
    grid = []
    for i in range(n):
        s = input().decode('utf-8')[:n]
        grid.append(s)

    ans = 0
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    accudp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for j in range(n):
        if grid[0][j] == '1':
            dp[0][j] = 1
            accudp[0][j] = 1
            ans += 1

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                curr = accudp[i - 1][j + 1] + dp[i - 1][j]
            elif j == n - 1:
                curr = accudp[i - 1][j - 1] + dp[i - 1][j]
            else:
                curr = accudp[i - 1][j - 1] + accudp[i - 1][j + 1] - accudp[i - 2][j] + dp[i - 1][j]
            accudp[i][j] = curr
            #            print(i,j,curr)

            if grid[i][j] == '1' and curr % 2 == 1:   continue
            if grid[i][j] == '0' and curr % 2 == 0:   continue
            dp[i][j] = 1
            accudp[i][j] += 1
            ans += 1

    #    print(dp)
    #    print(accudp)

    print(ans)


T = int(input())
t = 1
while t <= T:
    main(t)
    t += 1
