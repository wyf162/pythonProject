import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 100
print(tcn)
for _tcn_ in range(tcn):
    n, m = 5, 5
    print(n, m)
    nums = [random.randint(1, 2) for _ in range(n)]
    print(*nums)
