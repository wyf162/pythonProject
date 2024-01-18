import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
nums = [LI() + [i + 1] for i in range(n)]
nums.sort(key=lambda x: (x[0] * 100000 / (x[0] + x[1]), -x[2]), reverse=True)
rst = [x[2] for x in nums]
print(*rst)
