import math
import sys

MODD = 1024
# sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# make it alternating

tcn = I()
for _ in range(tcn):
    s = input()

    ret = 0
    ans = 1
    n = 1
    m = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            n += 1
            ret += 1
        else:
            ans *= n
            ans %= MODD
            m += (n - 1)
            n = 1

    ans *= n
    ans %= MODD
    m += (n - 1)
    ans *= math.factorial(m)
    ans %= MODD
    print(ret, ans)
