import sys

sys.stdin = open('./input.txt', 'r')
# sys.stdin = open('./i1.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

ts = [int(x) for x in input().split()[1:]]
dists = [int(x) for x in input().split()[1:]]
print(ts)
print(dists)

rst = 1
for t, d in zip(ts, dists):
    res = 0
    for i in range(t + 1):
        td = i * (t - i)
        # print(td)
        if td > d:
            res += 1
    print(res)
    rst *= res

print(rst)
