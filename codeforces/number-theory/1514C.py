import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()

nums = []
tot = 1
for num in range(1, n):
    if math.gcd(num, n) == 1:
        nums.append(num)
        tot *= num
        tot %= n

if tot != 1 and tot in nums:
    nums.remove(tot)
print(len(nums))
print(*nums)
