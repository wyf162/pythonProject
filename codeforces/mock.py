import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 100
print(tcn)
for _tcn_ in range(tcn):
    N = 10
    n = 3
    m = 3
    k = 10
    print(n, m, k)
    X = [0] + random.sample(range(1, N), n - 2) + [N]
    Y = [0] + random.sample(range(1, N), m - 2) + [N]
    X.sort()
    Y.sort()
    print(*X)
    print(*Y)
    st = set()
    i = 0
    while i < k:
        x1, y1 = random.randint(0, N ), random.randint(0, N )
        if (x1, y1) not in st and (x1 in X or y1 in Y):
            print(x1, y1)
            i += 1
            st.add((x1, y1))
    # print(*a)
    # for i in range(m):
    #     print(random.randint(1, 2), random.randint(1, 10))
