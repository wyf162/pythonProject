# ABC332E Lucky bag  O(3^N)
# Reference: https://atcoder.jp/contests/abc332/editorial/7947

import sys
sys.stdin = open('../../input.txt')
# 入力受取
N, D = map(int, input().split())
W = list(map(int, input().split()))

# sub[S]: 集合S(二進数表記)をひとつの集合としたときの、(重さの総和 - 平均) ** 2
# 先に集合Sの重さの総和を計算してから変換することでO(2^N)
has_bit = lambda S, x: S >> x & 1
sub = [0] * (1 << N)
bitcnt = [0] * (1 << N)
for i in range(N):
    for S in range(1 << i):
        sub[S | 1 << i] = sub[S] + W[i]
        bitcnt[S | 1 << i] = bitcnt[S] + 1

ave = sub[-1] / D
for S in range(1 << N):
    sub[S] = (sub[S] - ave) ** 2

# DP[S]: d袋採用後の残りが集合Sとなるときの、Σ(xi - ave) ** 2 の最小値
#       ただし、d袋採用時点で{N-d, N-d+1, ... , N-1} は必ず採用済でないといけない。
DP = [(1 << 62) - 1.0 for _ in range(1 << N)]
DP[-1] = 0  # 初期状態では全部残っている

# d袋目を入れる
for d in range(1, D + 1):
    for S in range(1 << (N - d)):  # 残る要素
        DP[S] = (1 << 62) - 1.0  # ひとつも採用しなかった遷移を潰しておく
        if bitcnt[S] < D - d: continue
        bit_mask = ((1 << (N - d + 1)) - 1) & ~S
        T = bit_mask  # 今回採用する要素
        while T > 0:
            T = T & bit_mask
            DP[S] = min(DP[S], DP[S + T] + sub[T])
            T -= 1

        # 答えを出力
print(DP[0] / D)
