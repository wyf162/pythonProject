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
A = LI()
B = LI()

tot = sum(a * b for a, b in zip(A, B))
# print(tot)
mx = 0
for i in range(n):
    delta = 0
    left, right = i, i + 1
    while left >= 0 and right < n:
        delta += (A[right] - A[left]) * (B[left] - B[right])
        mx = max(mx, delta)
        left -= 1
        right += 1

for i in range(n):
    delta = 0
    left, right = i, i + 2
    while left >= 0 and right < n:
        delta += (A[right] - A[left]) * (B[left] - B[right])
        mx = max(mx, delta)
        left -= 1
        right += 1

print(tot + mx)
