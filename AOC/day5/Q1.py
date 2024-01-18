import sys

sys.stdin = open('./input.txt', 'r')
# sys.stdin = open('./i1.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

s = input()
seeds = [int(x) for x in s[7:].split()]
cvs = [[] for i in range(7)]
nums = [17, 9, 40, 24, 20, 44, 41]
# nums = [2, 3, 4, 2, 3, 2, 2]
for i in range(7):
    input()
    input()
    cvs[i] = [LI() for _ in range(nums[i])]

for cv in cvs:
    for i, seed in enumerate(seeds):
        for dest, src, rng in cv:
            if src <= seed < src + rng:
                seeds[i] = dest + seed - src
                break

rst = min(seeds)
print(rst)

