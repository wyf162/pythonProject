from math import factorial as f

n = int(input())
arr = list(map(int, input().split()))
p = 1
for i in range(0, n, 3):
    a = arr[i:i + 3]
    p *= a.count(min(a))
print(f(n // 3) // (f(n // 6) ** 2) * p % 998244353)
