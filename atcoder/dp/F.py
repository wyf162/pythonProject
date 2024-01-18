import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

s = input()
t = input()
n, m = len(s), len(t)

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(n):
    for j in range(m):
        dp[i + 1][j + 1] = max(dp[i][j] + int(s[i] == t[j]), dp[i + 1][j], dp[i][j + 1])

for i in range(n + 1):
    print(dp[i])

i, j = n, m
ans = ''
while i > 0 and j > 0:
    if dp[i][j] - dp[i - 1][j - 1] == 1 and s[i - 1] == t[j - 1]:
        ans = s[i - 1] + ans
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        i -= 1
        j -= 1
print(ans)

# bx
# xaa
#
# xaa
# bx
