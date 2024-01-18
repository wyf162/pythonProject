import sys
from collections import Counter
from functools import cmp_to_key

N = 1000
sys.stdin = open('./input.txt', 'r')
# N = 5
# sys.stdin = open('./demo.txt', 'r')

ab = []
for _ in range(N):
    s, x = input().split()
    ab.append([s, int(x)])

S = '123456789TJQKA'


def convert(s):
    cnt = [0] * 14
    for c in s:
        cnt[S.index(c)] += 1

    xs = [[] for _ in range(6)]

    for i in range(13, 0, -1):
        if cnt[i]:
            xs[cnt[i]].append(i)
    if xs[5]:
        return 7
    if xs[4]:
        return 6
    if xs[3] and xs[2]:
        return 5
    if xs[3]:
        return 4
    if len(xs[2]) >= 2:
        return 3
    if xs[2]:
        return 2
    return 1


def cmp(s1, s2):
    xs1 = convert(s1[0])
    xs2 = convert(s2[0])

    if xs1 > xs2:
        return 1
    elif xs1 < xs2:
        return -1
    else:
        for i in range(5):
            j1, j2 = S.index(s1[0][i]), S.index(s2[0][i])
            if j1 > j2:
                return 1
            elif j1 < j2:
                return -1
        return 0


B = sorted(ab, key=cmp_to_key(cmp))
print(B)
rst = 0
for i in range(N):
    rst += B[i][1] * (i + 1)
print(rst)
