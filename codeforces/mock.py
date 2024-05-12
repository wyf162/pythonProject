import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 1000
print(tcn)
for _tcn_ in range(tcn):
    n = 10
    print(n)
    nums = [random.randint(1, 100) for i in range((n))]
    print(*nums)

