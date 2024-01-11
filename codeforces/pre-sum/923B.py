import bisect
import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N = I()
V = LI()
T = LI()
ans = [0] * (N + 2)

pre_sum = [0] * (N + 1)
for i in range(N):
    pre_sum[i + 1] = pre_sum[i] + T[i]

diff = [0] * (N + 2)
for i in range(N):
    j = bisect.bisect_right(pre_sum, pre_sum[i] + V[i])
    diff[i] += 1
    diff[j - 1] -= 1
    ans[j - 1] += V[i] - (pre_sum[j - 1] - pre_sum[i])

x = 0
for i in range(N):
    x += diff[i]
    ans[i] += T[i] * x

print(*ans[:N])

# ans = [0] * N
# for i in range(N):
#     for j in range(i + 1):
#         if V[j] > T[i]:
#             V[j] -= T[i]
#             ans[i] += T[i]
#         else:
#             ans[i] += V[j]
#             V[j] = 0
# print(*ans)
