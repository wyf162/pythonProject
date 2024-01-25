import math
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

n, m = MI()
a = LI()
b = LI()

c = [0] * 32
for x in b:
    c[x] += 1

d = [0] * 32
for x in a:
    for i in range(32):
        if x >> i & 1:
            d[i] += 1

tot = 0
for i in range(32):
    if c[i] <= d[i]:
        tot += c[i]
        d[i] -= c[i]
    else:
        k = c[i] - d[i]
        tot += d[i]
        d[i] = 0
        for j in range(i + 1, 32):
            if d[j] >= math.ceil(k / (1 << (j - i))):
                tot += k
                d[j] -= math.ceil(k / (1 << (j - i)))

                x =  math.ceil(k / (1 << (j - i))) * (1 << j) - k * (1 << i)
                if x:
                    d[x.bit_length()-1] += 1
                break
            else:
                k -= d[j] << (j - i)
                tot += d[j] << (j - i)
                d[j] = 0

print(tot)
