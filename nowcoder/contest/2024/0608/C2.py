# -*- coding : utf-8 -*-
# @Time: 2024/6/8 14:28
# @Author: yefei.wang
# @File: C2.py
import sys
from math import inf

import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar('T')


class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket: n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b + 1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


class RangeChangeRangeSumMinMax:
    def __init__(self, n):
        self.n = n
        self.cover = [0] * (4 * self.n)  # range sum
        self.lazy = [inf] * (4 * self.n)  # because range change can to be 0 the lazy tag must be inf
        self.floor = [inf] * (4 * self.n)  # because range change can to be any integer the floor initial must be inf
        self.ceil = [-inf] * (4 * self.n)  # because range change can to be any integer the ceil initial must be -inf
        return

    @staticmethod
    def _max(a, b):
        return a if a > b else b

    @staticmethod
    def _min(a, b):
        return a if a < b else b

    def _push_down(self, i, s, m, t):
        if self.lazy[i] != inf:
            self.cover[2 * i] = self.lazy[i] * (m - s + 1)
            self.cover[2 * i + 1] = self.lazy[i] * (t - m)

            self.floor[2 * i] = self.lazy[i]
            self.floor[2 * i + 1] = self.lazy[i]

            self.ceil[2 * i] = self.lazy[i]
            self.ceil[2 * i + 1] = self.lazy[i]

            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]

            self.lazy[i] = inf

    def _push_up(self, i) -> None:
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        self.ceil[i] = self._max(self.ceil[2 * i], self.ceil[2 * i + 1])
        self.floor[i] = self._min(self.floor[2 * i], self.floor[2 * i + 1])
        return

    def _make_tag(self, i, s, t, val) -> None:
        self.cover[i] = val * (t - s + 1)
        self.floor[i] = val
        self.ceil[i] = val
        self.lazy[i] = val
        return

    def build(self, nums):
        stack = [(0, self.n - 1, 1)]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self._make_tag(ind, s, t, nums[s])
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self._push_up(ind)
        return

    def get(self):
        stack = [(0, self.n - 1, 1)]
        nums = [0] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                nums[s] = self.cover[i]
                continue
            m = s + (t - s) // 2
            self._push_down(i, s, m, t)
            stack.append((s, m, 2 * i))
            stack.append((m + 1, t, 2 * i + 1))
        return nums

    def range_change(self, left, right, val):
        # update the range change
        assert 0 <= left <= right <= self.n - 1
        stack = [(0, self.n - 1, 1)]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self._make_tag(i, s, t, val)
                    continue

                m = s + (t - s) // 2
                self._push_down(i, s, m, t)
                stack.append((s, t, ~i))

                if left <= m:
                    stack.append((s, m, 2 * i))
                if right > m:
                    stack.append((m + 1, t, 2 * i + 1))
            else:
                i = ~i
                self._push_up(i)
        return

    def range_sum(self, left, right):
        # query the range sum
        assert 0 <= left <= right <= self.n - 1
        stack = [(0, self.n - 1, 1)]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            self._push_down(i, s, m, t)
            if left <= m:
                stack.append((s, m, 2 * i))
            if right > m:
                stack.append((m + 1, t, 2 * i + 1))
        return ans

    def range_min(self, left, right):
        # query the range min
        assert 0 <= left <= right <= self.n - 1
        stack = [(0, self.n - 1, 1)]
        lowest = inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                lowest = self._min(lowest, self.floor[i])
                continue
            m = s + (t - s) // 2
            self._push_down(i, s, m, t)
            if left <= m:
                stack.append((s, m, 2 * i))
            if right > m:
                stack.append((m + 1, t, 2 * i + 1))
        return lowest

    def range_max(self, left, right):
        # query the range max
        assert 0 <= left <= right <= self.n - 1
        stack = [(0, self.n - 1, 1)]
        highest = -inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self._max(highest, self.ceil[i])
                continue
            m = s + (t - s) // 2
            self._push_down(i, s, m, t)
            if left <= m:
                stack.append((s, m, 2 * i))
            if right > m:
                stack.append((m + 1, t, 2 * i + 1))
        return highest


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m, q = MI()
X = LI()
V = LI()
ops = [LI() for _ in range(q)]

Lst = RangeChangeRangeSumMinMax(n + 1)

for i in range(1, m):
    l, r = X[i - 1], X[i]
    Lst.range_change(l, l, 0)
    if l + 1 <= r - 1:
        Lst.range_change(l + 1, r - 1, V[i] * V[i - 1])
Lst.range_change(n, n, 0)

# for i in range(1, n + 1):
#     print(Lst.range_sum(i, i), end=' ')

st = SortedSet(X)
hst = {x: v for x, v in zip(X, V)}

for op in ops:
    if op[0] == 1:
        mid = op[1]
        l = st.lt(mid)
        r = st.gt(mid)
        hst[mid] = op[2]
        if l + 1 <= mid - 1:
            Lst.range_change(l + 1, mid - 1, hst[l] * hst[mid])
        Lst.range_change(mid, mid, 0)
        if mid + 1 <= r - 1:
            Lst.range_change(mid + 1, r - 1, hst[r] * hst[mid])
        st.add(mid)
    else:
        l, r = op[1], op[2]
        ans = Lst.range_sum(l, r)
        print(ans)
