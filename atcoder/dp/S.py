import sys

sys.stdin = open('./../input.txt', 'r')


class mint(int):
    MOD = 10 ** 9 + 7

    def __add__(self, other):
        return mint(int.__add__(self, other) % self.MOD)

    def __sub__(self, other):
        return mint(int.__sub__(self, other) % self.MOD)

    def __mul__(self, other):
        return mint(int.__mul__(self, other) % self.MOD)

    def __truediv__(self, other):
        return mint(int.__mul__(self, pow(other, -1, self.MOD)) % self.MOD)


K = list(map(int, list(input())))
N = len(K)
D = int(input())
dp = [[[mint(0)] * 2 for i in range(D)] for j in range(N + 1)]
dp[0][0][0] = mint(1)
for i in range(N):
    for d in range(D):
        a = K[N - 1 - i]
        for j in range(10):
            if j <= a:
                dp[i + 1][(d + j) % D][0] += dp[i][d][0]
            else:
                dp[i + 1][(d + j) % D][1] += dp[i][d][0]

            if j < a:
                dp[i + 1][(d + j) % D][0] += dp[i][d][1]
            else:
                dp[i + 1][(d + j) % D][1] += dp[i][d][1]
print(dp[N][0][0] - 1)

# @lru_cache(None)
# def dfs(i: int, s: int, is_limit: bool, is_num: bool) -> int:
#     if i == len(k):
#         return int(s > 0 and s % D == 0)
#     ret = 0
#
#     if not is_num:
#         ret += dfs(i + 1, s, False, False)
#
#     low = 0 if is_num else 1
#     up = int(k[i]) if is_limit else 9
#     for x in range(low, up + 1):
#         ret += dfs(i + 1, s + x, is_limit and x == int(k[i]), True)
#         ret %= mod
#     return ret
#
#
# rst = dfs(0, 0, True, False)

# print(rst)
