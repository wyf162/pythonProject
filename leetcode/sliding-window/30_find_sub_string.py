# _*_ coding: utf-8 _*_
# @Time : 2022/3/26 下午12:22 
# @Author : wangyefei
# @File : 30_find_sub_string.py
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(words), len(words[0])
        target_hst = dict()
        ret = list()
        for word in words:
            target_hst[word] = 1 + target_hst.get(word, 0)
        for i in range(n):
            cur_hst = dict()
            for j in range(i, i + m * n, n):
                word = s[j:j + n]
                cur_hst[word] = 1 + cur_hst.get(word, 0)
            if cur_hst == target_hst:
                ret.append(i)
            for j in range(i + m * n, len(s), n):
                remove_word = s[j - m * n:j - m * n + n]
                cur_hst[remove_word] -= 1
                if cur_hst[remove_word] == 0:
                    del cur_hst[remove_word]
                add_word = s[j:j + n]
                cur_hst[add_word] = 1 + cur_hst.get(add_word, 0)
                if cur_hst == target_hst:
                    ret.append(j - m * n + n)
        return ret


if __name__ == '__main__':
    sol = Solution()
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    ret = sol.findSubstring(s, words)
    print(ret)
