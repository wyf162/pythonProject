import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
b = LI()
b.append(b[-1])
i, j = 0, 0
c = [m - 1] * n
while i < n and j < m:
    c[i] = j
    if a[i] < b[j]:
        i += 1
    else:
        j += 1

rst = 0
for i in range(n):
    tmp = min(abs(a[i] - b[c[i]]), abs(a[i] - b[c[i] - 1]), abs(a[i] - b[c[i] + 1]))
    rst = max(tmp, rst)

print(rst)
