
from typing import List

s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = s1[1:] + s1[0]
hst = {c1: c2 for c1, c2 in zip(s1, s2)}


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        path = bin(k-1)[2:][::-1]
        print(path)
        cur = 'a'
        for i, c in enumerate(path):
            if c == '1' and operations[i] == 1:
                cur = hst[cur]
        return cur


if __name__ == "__main__":
    sol = Solution()
    k = 3
    operations = [1, 0, 0, 1]
    ret = sol.kthCharacter(k, operations)
    print(ret)
