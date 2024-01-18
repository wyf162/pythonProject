# N = int(input())
# S = input()
#
# for i in range(N - 1):
#     if int(S[i]) >= 2 and int(S[i + 1]) >= 2:
#         print(-1)
#         exit()
#
# MOD = 998244353
# ans = 0
#
# for i in reversed(range(1, N)):
#     ans += 1
#     ans *= int(S[i])
#     ans %= MOD
# print(ans)
N = int(input())
S = input()

for i in range(N - 1):
    if int(S[i]) > 1 and int(S[i + 1]) > 1:
        print(-1)
        exit()

res = 1
mod = 998244353
for i in range(N - 2, -1, -1):
    res = res + int(S[i + 1]) + (int(S[i + 1]) - 1) * (res - 1)
    res %= mod
print(res - 1)
