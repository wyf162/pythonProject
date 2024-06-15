import random
import sys

sys.stdout = open('./input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 1000
print(tcn)
for _tcn_ in range(tcn):
    n = 10
    p = 10
    k = 2
    print(n, p, k)
    nums = [random.randint(1, 10) for _ in range(n)]
    print(*nums)
