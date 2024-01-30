import sys

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, w, h = MI()
wh = [LI() + [i] for i in range(n)]
dp = [0] * n
fa = [-1] * n
wh.sort()
for i in range(n):
    if wh[i][0] > w and wh[i][1] > h:
        dp[i] = 1
        fa[i] = -1
    for j in range(i):
        if dp[j] and wh[i][0] > wh[j][0] and wh[i][1] > wh[j][1]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                fa[i] = j

mx = max(dp)
if mx == 0:
    exit(print(0))
k = n - 1
while k >= 0:
    if dp[k] == mx:
        break
    k -= 1

paths = []
while k >= 0:
    paths.insert(0, wh[k][2] + 1)
    k = fa[k]
print(mx)
print(' '.join(map(str, paths)))
