# -*- coding: utf-8 -*-
# @Time: 2024/4/8 17:05
# @Author: yfwang
# @File: 1923E.py
# https://codeforces.com/contest/1923/problem/E
# trees

import sys

input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    C = list(map(int, input().split()))

    E = [[] for i in range(n)]

    for i in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        E[x].append(y)
        E[y].append(x)

    ROOT = 0

    QUE = [ROOT]
    Parent = [-1] * n
    Parent[ROOT] = n  # ROOTの親を定めておく.
    Child = [[] for i in range(n)]
    TOP_SORT = []  # トポロジカルソート

    while QUE:  # トポロジカルソートと同時に親を見つける
        x = QUE.pop()
        TOP_SORT.append(x)
        for to in E[x]:
            if Parent[to] == -1:
                Parent[to] = x
                Child[x].append(to)
                QUE.append(to)

    ANS = 0

    DP = [dict() for i in range(n)]

    for x0 in TOP_SORT[::-1]:
        if Child[x0] == []:
            DP[x0] = {C[x0]: 1}
            continue

        color = C[x0]

        dp = dict()

        for c in Child[x0]:
            dp2 = DP[c]

            if len(dp) < len(dp2):
                for x in dp:
                    if x == color:
                        ANS += dp[x]
                    else:
                        if x in dp2:
                            ANS += dp[x] * dp2[x]
                            dp2[x] += dp[x]
                        else:
                            dp2[x] = dp[x]
                dp = dp2
                DP[c] = dict()

            else:
                for x in dp2:
                    if x == color:
                        ANS += dp2[x]
                    else:
                        if x in dp:
                            ANS += dp[x] * dp2[x]
                            dp[x] += dp2[x]
                        else:
                            dp[x] = dp2[x]
                DP[c] = dict()

        if color in dp:
            ANS += dp[color]

        dp[color] = 1
        DP[x0] = dp
        # print(x,DP)

    print(ANS)
