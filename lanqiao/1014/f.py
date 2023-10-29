# -*- coding : utf-8 -*-
# @Time: 2023/10/14 20:00
# @Author: yefei.wang
# @File: f.py

def get_sum(x):
    total_sum = 0
    while x > 0:
        total_sum += sumf[x]
        x -= (x & -x)
    return total_sum


def update(pos, val):
    while pos < N:
        sumf[pos] += val
        pos += (pos & -pos)


def L_to_R():
    for i in range(1, N):
        for r in posL[i]:
            update(r, 1)

        for b, id in query[i]:
            if b > i:
                ans[id] = get_sum(b - 1)

        update(i, -len(posR[i]))


def R_to_L():
    for i in range(N - 1, 0, -1):
        for l in posR[i]:
            update(l, 1)

        for b, id in query[i]:
            if b < i:
                ans[id] = get_sum(N - 1) - get_sum(b)

        update(i, -len(posL[i]))


def sol():
    global N, posL, posR, query, ans, sumf
    n, q = map(int, input().split())
    N = 200100
    posL = [[] for _ in range(N)]
    posR = [[] for _ in range(N)]
    query = [[] for _ in range(N)]
    ans = [0] * N

    for _ in range(n):
        l, r = map(int, input().split())
        posL[l].append(r)
        posR[r].append(l)

    for i in range(q):
        a, b = map(int, input().split())
        query[a].append((b, i + 1))

    sumf = [0] * N
    L_to_R()
    sumf = [0] * N
    R_to_L()

    for i in range(1, q + 1):
        print(ans[i])


if __name__ == "__main__":
    T = 1
    while T > 0:
        sol()
        T -= 1