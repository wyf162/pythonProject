import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

t = input()
p = input()
a = LI()

n = len(t)


def check(mid):
    j = 0
    s = [''] * n
    for x in range(mid, n):
        i = a[x] - 1
        s[i] = t[i]
    for i in range(n):
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                return True
    return False


ans = 0
l, r = 0, n
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
