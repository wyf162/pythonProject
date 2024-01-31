import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def main():
    n = I()
    d = 0
    for i in range(n):
        A = LI()
        g = [[] for _ in range(A[0])]
        for j in range(A[0] - 1):
            u = A[j * 2 + 1] - 1
            v = A[j * 2 + 2] - 1
            g[u].append(v)
            g[v].append(u)

        def bfs(start):
            q = deque([(start, -1)])
            step = -1
            while q:
                step += 1
                for _ in range(len(q)):
                    x, fa = q.popleft()
                    for y in g[x]:
                        if y != fa:
                            q.append((y, x))
            return step, x

        mx1, v1 = bfs(0)
        mx2, v2 = bfs(v1)
        d += mx2
    print(d)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
