import sys
from collections import Counter

# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = input()
    cnt = Counter(s)
    mx = max(cnt.values())
    if n % 2 or mx * 2 > n:
        print(-1)
        continue

    cnt = Counter()
    for i in range(n >> 1):
        if s[i] == s[n - 1 - i]:
            cnt[s[i]] += 1
    tot = mx = 0
    if cnt:
        tot = sum(cnt.values())
        mx = max(cnt.values())
    if mx * 2 > tot:
        print(mx)
    else:
        print((tot + 1) // 2)
