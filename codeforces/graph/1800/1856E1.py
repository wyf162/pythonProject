''' E1. PermuTree (easy version)
https://codeforces.com/contest/1856/problem/E1
'''

import io, os, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def debug(*args):
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def solve(N, P):
    adj = [[] for _ in range(N)]
    for u, v in enumerate(P):
        u += 1;
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    res = 0
    size = [1] * N

    @bootstrap
    def dfs(u, p=-1):
        S = 0
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u)
            S += size[v]
        size[u] = S + 1

        dp = [1] + [0] * S
        mx = 0
        for v in adj[u]:
            if v == p: continue
            for s in range(S, -1, -1):
                if s - size[v] >= 0 and dp[s - size[v]]:
                    dp[s] = 1
                    mx = max(mx, s * (S - s))
        nonlocal res
        res += mx
        yield None

    dfs(0)
    return res


def main():
    N = int(input())
    P = list(map(int, input().split()))
    res = solve(N, P)
    print(res)


if __name__ == '__main__':
    main()
