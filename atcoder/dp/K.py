import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

N, K = MI()
A = LI()

dp = [False for i in range(K * 2 + 1000)]
for i in range(K):
    for a in A:
        if not dp[i]:
            dp[i + a] = True

print('First' if dp[K] == True else 'Second')
