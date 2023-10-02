# -*- coding : utf-8 -*-
# @Time: 2023/9/30 20:22
# @Author: yefei.wang
# @File: e.py


import sys
from typing import List

sys.stdin = open('./../../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

inf = float('inf')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, K, P = MI()
plans = [LI() for _ in range(N)]

MX = (P + 1) ** K - 1


def state2idx(state: List[int]) -> int:
    idx = 0
    for i, param in enumerate(state):
        idx += param * P ** i
    return idx if idx <= MX else MX


def idx2state(idx: int):
    state = []
    for i in range(K):
        state.append(idx % (P+1))
        idx = idx // (P+1)
    return state


def idx_add_plan(idx_, plan_):
    state = idx2state(idx_)
    for i in range(K):
        state[i] = min(state[i] + plan_[i], P)
    next_idx = state2idx(state)
    return next_idx


def idx_sub_plan(idx_, plan_):
    state = idx2state(idx_)
    for i in range(K):
        state[i] = max(state[i] - plan_[i], 0)
    next_idx = state2idx(state)
    return next_idx


def check(state2, state1):
    for i in range(K):
        if state2[i] < state1[i]:
            return False
    return True


dp = [inf] * (MX + 1)
dp[0] = 0

for plan in plans:
    c = plan[0]
    for idx in range(MX, 0, -1):
        state = idx2state(idx)
        print(state)
        if check(state, plan[1:]):
            nidx = idx_sub_plan(idx, plan[1:])
            print(state, nidx)
            dp[idx] = min(dp[nidx] + c, dp[idx])

print(dp[-1])
