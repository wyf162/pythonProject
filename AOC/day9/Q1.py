import sys

N = 3
sys.stdin = open('./demo.txt', 'r')
# N = 200
# sys.stdin = open('./input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

ans = 0

for _ in range(N):
    a = LI()
    nn = [a]
    while True:
        b = []
        for i in range(1, len(nn[-1]), 1):
            b.append(nn[-1][i] - nn[-1][i - 1])
        nn.append(b)
        # if all(x == 0 for x in b):
        #     break
        if sum(b) == 0:
            break
    rst = 0
    for i in range(len(nn) - 1, -1, -1):
        rst += nn[i][-1]
    print(rst)
    ans += rst

print(ans)

# 1921197370