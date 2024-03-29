class Dual_Segment_Tree:
    def __init__(self, L, comp, id):
        """ comp を演算とするリスト L の Dual Segment Tree を作成

        comp : 作用素
        id : 単位元

        [注記]
        更新は左から. つまり, comp(new, old) となる.
        """

        self.comp = comp
        self.id = id

        N = len(L)
        d = max(1, (N - 1).bit_length())
        k = 1 << d

        self.lazy = [self.id] * k + L + [self.id] * (k - N)
        self.N = k
        self.depth = d

    # 配列の第 m 要素を下に伝搬
    def _propagate_at(self, m):
        lazy = self.lazy
        if lazy[m] != self.id:
            lazy[(m << 1) | 0] = self.comp(lazy[m], lazy[(m << 1) | 0])
            lazy[(m << 1) | 1] = self.comp(lazy[m], lazy[(m << 1) | 1])
            lazy[m] = self.id

    # 配列の第 m 要素より上を全て伝搬
    def _propagate_above(self, m):
        H = m.bit_length()
        for h in range(H - 1, 0, -1):
            self._propagate_at(m >> h)

    # 作用
    def action(self, l, r, alpha, left_closed=True, right_closed=True):
        L = l + self.N + (not left_closed)
        R = r + self.N + (right_closed)

        L0 = R0 = -1
        X, Y = L, R - 1
        while X < Y:
            if X & 1:
                L0 = max(L0, X)
                X += 1

            if Y & 1 == 0:
                R0 = max(R0, Y)
                Y -= 1

            X >>= 1
            Y >>= 1

        L0 = max(L0, X)
        R0 = max(R0, Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        lazy = self.lazy;
        comp = self.comp
        while L < R:
            if L & 1:
                lazy[L] = comp(alpha, lazy[L])
                L += 1

            if R & 1:
                R -= 1
                lazy[R] = comp(alpha, lazy[R])

            L >>= 1
            R >>= 1

    # リフレッシュ
    def refresh(self):
        for m in range(1, self.N):
            self._propagate_at(m)

    # 取得
    def get(self, k):
        m = k + self.N
        self._propagate_above(m)
        return self.lazy[m]

    def __getitem__(self, index):
        m = index + self.N
        self._propagate_above(m)
        return self.lazy[m]

    def __setitem__(self, index, value):
        self.action(index, index, value)


def encode(a, b):
    return a * 10 ** 9 + b


def decode(code):
    return divmod(code, 10 ** 9)


def solve():
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    Mod = 998244353

    id = encode(1, 0)

    def comp(g, f):
        fa, fb = decode(f)
        ga, gb = decode(g)

        ha = fa * ga % Mod
        hb = (fb * ga + gb) % Mod
        return encode(ha, hb)

    S = Dual_Segment_Tree([id] * (N + 1), comp, id)

    inv = [0] * (N + 1);
    inv[1] = 1
    for i in range(2, N + 1):
        q, r = divmod(Mod, i)
        inv[i] = - q * inv[r] % Mod

    for _ in range(M):
        L, R, X = map(int, input().split())

        d = R - L + 1
        a = (d - 1) * inv[d] % Mod
        b = X * inv[d] % Mod
        S.action(L, R, encode(a, b))

    E = [0] * (N + 1)
    for i in range(N + 1):
        a, b = decode(S.get(i))
        E[i] = (a * A[i] + b) % Mod
    return E[1:]


# ==================================================
import sys

input = sys.stdin.readline
write = sys.stdout.write

print(*solve())
