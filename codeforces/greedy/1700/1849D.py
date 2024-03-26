# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
ss = []
i = 0
cost = [1] * n
two = False

for j in range(n):
    if a[j] > 0:
        cost[j] = 0
        if a[j] > 1:
            two = True
        continue
    else:
        if j - 1 >= i:
            ss.append([i, j - 1, two])
        i = j + 1
        two = False

if n-1 >= i:
    ss.append([i, n - 1, two])

for x, y, two in ss:
    if two:
        if x - 1 >= 0:
            cost[x - 1] = 0
        if y + 1 < n:
            cost[y + 1] = 0
    else:
        if x - 1 >= 0 and cost[x - 1]:
            cost[x - 1] = 0
        elif y + 1 < n and cost[y + 1]:
            cost[y + 1] = 0

ans = len(ss) + sum(cost)
print(ans)
