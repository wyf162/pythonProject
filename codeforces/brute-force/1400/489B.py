import sys

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
nums1 = LI()
m = I()
nums2 = LI()

nums1.sort()
nums2.sort()

cnt = 0
pt = 0

for num in nums1:
    while pt < m and nums2[pt] < num - 1:
        pt += 1
    if pt < m and abs(nums2[pt] - num) <= 1:
        cnt += 1
        pt += 1

print(cnt)

