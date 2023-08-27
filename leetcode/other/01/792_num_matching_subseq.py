# _*_ coding: utf-8 _*_
# @Time : 2022/11/17 10:06 PM 
# @Author : yefe
# @File : 792_num_matching_subseq


from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        next_vector = [[None for j in range(26)] for i in range(n)]
        nexts = [None] * 26
        for i in range(n - 1, -1, -1):
            for j, v in enumerate(nexts):
                next_vector[i][j] = v
            nexts[ord(s[i]) - ord('a')] = i

        ans = 0
        for word in words:
            idx = 1
            cur = nexts[ord(word[0]) - ord('a')]
            while cur is not None and idx < len(word):
                cur = next_vector[cur][ord(word[idx]) - ord('a')]
                idx += 1

            if idx == len(word) and cur is not None:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    ret = sol.numMatchingSubseq(s, words)
    print(ret)
