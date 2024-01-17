import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 100
print(tcn)
for _tcn_ in range(tcn):
    n = 1000
    print(n)
    nums = [random.randint(-1000, 1000)*2 for _ in range(n)]
    nums = [x+2 if x==0 else x for x in nums]
    print(*nums)
