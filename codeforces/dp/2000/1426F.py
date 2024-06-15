# -*- coding : utf-8 -*-
# @Time: 2024/6/15 18:31
# @Author: yefei.wang
# @File: 1426F.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    pow3 = [1]
    for i in range(n):
        pow3.append(pow3[-1] * 3 % mod)

    s = input()
    PA = [0] * (n + 1)
    PD = [0] * (n + 1)
    for i in range(n):
        PA[i + 1] = PA[i] + int(s[i] == 'a')
        PD[i + 1] = PD[i] + int(s[i] == '?')

    SC = [0] * (n + 1)
    SD = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        SC[i] = SC[i + 1] + int(s[i] == 'c')
        SD[i] = SD[i + 1] + int(s[i] == '?')

    ans = 0
    for i in range(1, n - 1):
        if s[i] == 'b' or s[i] == '?':
            ans += PA[i] * SC[i + 1] * pow3[PD[i] + SD[i + 1]] % mod
            ans += PD[i] * SC[i + 1] * pow3[PD[i] - 1 + SD[i + 1]] % mod
            ans += PA[i] * SD[i + 1] * pow3[PD[i] + SD[i + 1] - 1] % mod
            ans += PD[i] * SD[i + 1] * pow3[PD[i] + SD[i + 1] - 2] % mod
    print(ans)
