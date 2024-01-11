# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()

for i in range(n):
    if a[i] >= 0:
        a[i] = -a[i] - 1

if n % 2 == 1:
    mi = min(a)
    for i in range(n):
        if a[i] == mi:
            a[i] = -a[i] - 1
            break
print(' '.join(map(str, a)))
