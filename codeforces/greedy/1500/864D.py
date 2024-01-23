import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
cnt = Counter(a)

p = 1
for i in range(n):
    while p in cnt:
        p += 1

    if cnt[a[i]] == 1:
        continue

    if cnt[a[i]] > 0 and a[i] < p:
        cnt[a[i]] = 0
        continue
    else:
        cnt[a[i]] -= 1
        a[i] = p
        p += 1

print(n-len(cnt))
print(' '.join(map(str, a)))

