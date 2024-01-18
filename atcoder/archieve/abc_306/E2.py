from heapq import heapify, heappush, heappop
from sys import stdin

input = stdin.readline
mask = (1 << 19) - 1

n, k, q = map(int, input().split())

big = list(range(k))
heapify(big)

big_deleted = []

small = list(range(-k, -n, -1))
heapify(small)

small_deleted = []

is_big = [1] * k + [0] * (n - k)
a = [0] * n

ans = [0] * q
tmp = 0

for i in range(q):
    x, y = map(int, input().split())
    x -= 1

    u = (a[x] << 19) | x
    v = (y << 19) | x

    if is_big[x]:
        heappush(big_deleted, u)
        tmp -= a[x]
        if k < n and v < -small[0]:
            is_big[x] = 0
            is_big[(-small[0]) & mask] = 1
            tmp += (-small[0]) >> 19
            heappush(big, -heappop(small))
            heappush(small, -v)
        else:
            tmp += y
            heappush(big, v)
    else:
        heappush(small_deleted, -u)
        if big[0] < v:
            is_big[big[0] & mask] = 0
            is_big[x] = 1
            tmp -= big[0] >> 19
            tmp += y
            heappush(small, -heappop(big))
            heappush(big, v)
        else:
            heappush(small, -v)

    a[x] = y
    ans[i] = tmp

    while big_deleted and big_deleted[0] == big[0]:
        heappop(big_deleted)
        heappop(big)
    while small_deleted and small_deleted[0] == small[0]:
        heappop(small_deleted)
        heappop(small)

print(*ans, sep='\n')
