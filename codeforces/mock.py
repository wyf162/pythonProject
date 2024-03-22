import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 100
print(tcn)
for _tcn_ in range(tcn):
    n = 10
    print(n)
    a = [random.randint(1, 10) for _ in range(n)]
    print(*a)
