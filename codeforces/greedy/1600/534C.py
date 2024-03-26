# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))

n, s = MI()
a = LI()

sa = sum(a)

ans = [0] * n
for i in range(n):
    k = sa - a[i]
    left = max(1, s - k)
    right = min(a[i], s - (n - 1))
    ans[i] = a[i] - (right - left + 1)
print(' '.join(map(str, ans)))
