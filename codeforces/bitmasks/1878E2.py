import sys

input = sys.stdin.readline


def init(n):
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i * 2] & tree[i * 2 + 1]


def update(n, w, v):
    w += n
    tree[w] += v
    while w > 1:
        tree[w // 2] = tree[w] + tree[w ^ 1]
        w //= 2


def get_sum(n, l, r):
    l += n
    r += n
    result = tree[l]
    while l < r:
        if l % 2:
            result &= tree[l]
            l += 1
        if r % 2:
            r -= 1
            result &= tree[r]
        l //= 2
        r //= 2
    return result


for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    tree = [0] * n + num
    init(n)
    ans = []
    for _ in range(int(input())):
        l, k = map(int, input().split())
        l -= 1
        if num[l] < k:
            ans.append(-1)
            continue
        lo, hi = l, n
        now = 0
        while lo <= hi:
            c = (lo + hi) // 2
            if get_sum(n, l, c) >= k:
                now = max(l, c)
                lo = c + 1
            else:
                hi = c - 1
        ans.append(now)
    print(*ans)
