import sys
from heapq import heappushpop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
nums = LI()
taken = []
tot = 0
for num in nums:
    tot += num
    if tot >= 0:
        heappush(taken, num)
    else:
        tot -= heappushpop(taken, num)

print(len(taken))
