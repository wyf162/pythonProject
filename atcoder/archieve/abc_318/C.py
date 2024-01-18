import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

N, D, P = MI()
a = LI()

a.sort(reverse=True)
pre_sum = [0] * (N + 1)
for i in range(N):
    pre_sum[i + 1] = pre_sum[i] + a[i]

ans = 0
for i in range(0, N + 1, D):
    j = min(i + D, N)
    if pre_sum[j] - pre_sum[i] > P:
        ans += P
    else:
        ans += pre_sum[j] - pre_sum[i]
print(ans)
