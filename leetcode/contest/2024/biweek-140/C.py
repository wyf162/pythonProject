
from typing import List
from functools import cache
import sys
sys.setrecursionlimit(10**6)


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        n1 = len(word1)
        n2 = len(word2)

        @cache
        def dfs(i1, i2, can_mismatch):
            if i2 == n2 or i1 == n1:
                return []
            if n2 - i2 > n1 - i1:
                return []
            if word1[i1] == word2[i2]:
                return [i1].extend(dfs(i1 + 1, i2 + 1, can_mismatch))
            if can_mismatch:
                ret1 = [i1].extend(dfs(i1 + 1, i2 + 1, False))
                if len(ret1) == n2 - i2:
                    return ret1
                ret2 = dfs(i1 + 1, i2, True)
                if len(ret2) == n2 - i2:
                    return ret2
                else:
                    return []
            else:
                return dfs(i1 + 1, i2, can_mismatch)

        ret = dfs(0, 0, True)
        return ret if len(ret) == n2 else []


if __name__ == "__main__":
    sol = Solution()
    word1 = "ab" * 2500
    word2 = "ab" * 2500
    ret = sol.validSequence(word1, word2)
    print(ret)
