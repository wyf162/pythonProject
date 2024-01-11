import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + a[i]


    def check(mid):

        for i in range(n):
            m = mid
            op = 0
            for j in range(i, n):
                if a[j] >= m:
                    return True
                op += m - a[j]
                m -= 1
                if op > k:
                    break
        return False


    L = max(a)
    R = L + k
    ans = L
    while L <= R:
        mid = (L + R) // 2
        # print(mid)
        if check(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)
