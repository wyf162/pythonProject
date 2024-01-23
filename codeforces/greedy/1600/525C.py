import sys

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
a.sort(reverse=True)
b = []
pre = a[0]
i = 1
while i < n:
    if a[i] == pre:
        b.append(a[i])
        i += 1
        if i < n:
            pre = a[i]
        i += 1
    elif a[i] == pre - 1:
        b.append(a[i])
        i += 1
        if i < n:
            pre = a[i]
        i += 1
    else:
        pre = a[i]
        i += 1
ans = 0
for i in range(0, len(b), 2):
    if i + 1 < len(b):
        ans += b[i] * b[i + 1]
print(ans)
