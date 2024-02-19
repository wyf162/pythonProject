import random
from collections import Counter
from typing import List

n = 10 ** 5
times = random.randint(100, 500)
mod = random.getrandbits(32)
powers = [1] * (n + 1)
for i in range(1, n + 1):
    powers[i] = powers[i - 1] * times % mod


class RollingHash:
    def __init__(self, s):
        self.pre = [0]
        for c in s:
            self.pre.append((self.pre[-1] * times + ord(c)) % mod)

        self.suf = [0]
        for i, c in enumerate(s[::-1]):
            self.suf.append((self.suf[-1] + ord(c) * powers[i]) % mod)

    def pre_substr(self, i):
        return self.pre[i]

    def suf_substr(self, i):
        return self.suf[i]


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = Counter()
        ans = 0
        for word in words:
            rh1 = RollingHash(word)
            n = len(word)
            for i in range(1, n + 1):
                if rh1.pre_substr(i) == rh1.suf_substr(i):
                    ans += cnt[rh1.pre_substr(i)]
            cnt[rh1.pre_substr(n)] += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # words = ["a", "aba", "ababa", "aa"]
    words = ["pa", "papa", "ma", "mama"]
    ret = sol.countPrefixSuffixPairs(words)
    print(ret)
