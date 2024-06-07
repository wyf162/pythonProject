# -*- coding : utf-8 -*-
# @Time: 2024/6/6 23:06
# @Author: yefei.wang
# @File: D.py

import sys

from typing import Sequence, List


def knuth_morris_pratt(text: Sequence, pattern: Sequence) -> List[int]:
    """
    Given two strings text and pattern, return the list of start indexes in text that matches with the pattern
    using knuth_morris_pratt algorithm.

    Args:
        text: Text to search
        pattern: Pattern to search in the text
    Returns:
        List of indices of patterns found

    Example:
        # >>> knuth_morris_pratt('hello there hero!', 'he')
        [0, 7, 12]

    If idx is in the list, text[idx : idx + M] matches with pattern.
    Time complexity of the algorithm is O(N+M), with N and M the length of text and pattern, respectively.
    """
    n = len(text)
    m = len(pattern)
    pi = [0 for i in range(m)]
    i = 0
    j = 0
    # making pi table
    for i in range(1, m):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
sys.stdout = open('../../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    ans = -1
    s = input()
    if s[0] == '1':
        s = '1' * k + '0' * k + s
    else:
        s = '0' * k + '1' * k + s
    n += 2 * k
    suf = s[-1]
    for i in range(n - 2, -1, -1):
        if s[i] == suf[-1]:
            suf += s[i]
        else:
            break
    if len(suf) == k:
        suf1 = '0' * (k * 2)
        ret1 = knuth_morris_pratt(s, suf1)
        if ret1:
            i1 = ret1[0] + k
            t = s[i1:] + s[:i1][::-1]
            ans = i1 - 2 * k
        else:
            suf2 = '1' * (k * 2)
            ret2 = knuth_morris_pratt(s, suf2)
            if ret2:
                i2 = ret2[0] + k
                t = s[i2:] + s[:i2][::-1]
                ans = i2 - 2 * k
            else:
                ans = n - 2 * k
                t = s
    elif len(suf) > k:
        t = '#'
    else:
        plc = '0' if s[-1] == '1' else '1'
        suf1 = plc + s[-1] * (k - len(suf)) + plc
        ret1 = knuth_morris_pratt(s, suf1)
        if ret1:
            i1 = ret1[0] + k - len(suf) + 1
            t = s[i1:] + s[:i1][::-1]
            ans = i1 - 2 * k

        else:
            suf2 = plc + s[-1] * (k + k - len(suf)) + plc
            ret2 = knuth_morris_pratt(s, suf2)
            if ret2:
                i2 = ret2[0] + k - len(suf) + 1
                t = s[i2:] + s[:i2][::-1]
                ans = i2 - 2 * k
            else:
                t = '#'

    cnt = len(s) // k
    c1 = cnt // 2
    c2 = cnt % 2
    # print(t)
    if t[0] == '0':
        tt = ('0' * k + '1' * k) * c1 + ('0' * k) * c2
        if tt == t:
            print(ans)
        else:
            print(-1)
    else:
        tt = ('1' * k + '0' * k) * c1 + ('1' * k) * c2
        if tt == t:
            print(ans)
        else:
            print(-1)
