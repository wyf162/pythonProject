import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

N = I()
H = LI()
A = LI()

HX = 2 * 10 ** 5 + 1
b = [0] * HX
t = [0] * (HX * 4)


def pushup(p):
    t[p] = max(t[p * 2], t[p * 2 + 1])


def build(s, e, p):
    m = s + (e - s >> 1)
    build(s, m, p * 2)
    build(m + 1, e, p * 2 + 1)
    pushup(p)


def update(l, r, c, s, e, p):
    if s == e:
        t[p] = c
        return
    m = s + (e - s >> 1)
    if l <= m:
        update(l, r, c, s, m, p * 2)
    if r > m:
        update(l, r, c, m + 1, e, p * 2 + 1)
    pushup(p)


def query(l, r, s, e, p):
    if l <= s and e <= r:
        return t[p]
    m = s + (e - s >> 1)
    ret = 0
    if l <= m:
        ret = max(ret, query(l, r, s, m, p * 2))
    if r > m:
        ret = max(ret, query(l, r, m + 1, e, p * 2 + 1))
    return ret


dp = [0] * N
dp[0] = A[0]
if b[H[0]] < dp[0]:
    b[H[0]] = dp[0]
    update(H[0], H[0], dp[0], 1, 2 * 10 ** 5, 1)

for i in range(1, N):
    x = query(1, H[i], 1, 2 * 10 ** 5, 1)
    dp[i] = x + A[i]
    if b[H[i]] < dp[i]:
        b[H[i]] = dp[i]
        update(H[i], H[i], dp[i], 1, 2 * 10 ** 5, 1)

print(max(dp))
