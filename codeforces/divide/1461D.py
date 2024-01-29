import bisect
import sys
from types import GeneratorType
from itertools import accumulate


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, q = MI()
    a = LI()
    a.sort()
    pre_sum = [0] + list(accumulate(a))
    queries = [I() for _ in range(q)]
    st = set()
    st.add(pre_sum[-1])


    @bootstrap
    def func(i, j):
        if i > j or a[i] == a[j]:
            yield
        if i == j:
            st.add(a[i])
            yield
        mid = (a[i] + a[j]) // 2
        k = bisect.bisect_right(a, mid, lo=i)
        st.add(pre_sum[k] - pre_sum[i])
        st.add(pre_sum[j + 1] - pre_sum[k])
        yield func(i, k - 1)
        yield func(k, j)
        yield

    func(0, n - 1)
    for v in queries:
        Yn(v in st)
