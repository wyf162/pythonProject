import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('../input.txt', 'r')
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
    p = LI()
    cnt = Counter(p)
    vs = list(cnt.values()) + [1]
    vs.sort(reverse=True)
    m = len(vs)
    ans = m
    ret = []
    for i in range(m):
        r = vs[i] - (m - i)
        if r > 0:
            ret.append(r)
    if not ret:
        print(ans)
        continue
    ret.sort(reverse=True)
    while ret:
        ans += 1
        t = []
        if ret[0] - 2 > 0:
            t.append(ret[0] - 2)
        for x in ret[1:]:
            if x - 1 > 0:
                t.append(x - 1)
        ret = t
        ret.sort(reverse=True)
    print(ans)
