# _*_ coding: utf-8 _*_
# @Time : 2022/4/7 下午11:35 
# @Author : wangyefei
# @File : 17022.py
from typing import List
from collections import defaultdict, deque


class Solution1:

    def check_translate(self, a: str, b: str) -> bool:  # 是否恰好有1位不同
        if len(a) != len(b):
            return False
        n = len(a)
        cnt = 0
        for i in range(n):
            if a[i] != b[i]:
                cnt += 1
        return cnt == 1

    def dfs(self, curWord: str, endWord: str, wordList: List[str]) -> bool:
        if curWord == endWord:  # 剪枝
            return True
        n = len(wordList)
        for i in range(n):
            if self.visited[i] == True or self.check_translate(curWord, wordList[i]) == False:
                continue
            self.visited[i] = True
            self.path.append(wordList[i])
            if self.dfs(wordList[i], endWord, wordList) == True:
                return True
            self.path.pop(-1)  # 半回溯
            # self.visited[i] = False      #不是单纯的回溯   因为之间是有循环的 不是一棵树  是一个有环图！！！！！！！！！！！！！！
        return False

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        n = len(wordList)
        self.visited = [False for _ in range(n)]
        self.path = [beginWord]
        if self.dfs(beginWord, endWord, wordList) == True:
            return self.path[:]
        else:
            return []


class Solution2:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # c++ 可以建图 点用ID表示  邻接表
        # 然而Python3 还是桶 切片  比较快  126  127 单词接龙
        words_set = set(wordList)
        if endWord not in words_set:
            return []
        words_set.add(beginWord)
        bucket = defaultdict(list)
        m = len(beginWord)
        for w in words_set:  # 恰相差一个字母的在同一个桶
            for i in range(m):  # 同一个单词可能在不同的桶
                bucket[w[:i] + '*' + w[i + 1:]].append(w)

        res = []
        Q = [[beginWord]]
        visited = set()  # 注意记忆化的位置！！！！！！！！！！！！！！！！！！！！！！！！！
        while Q:
            cur_len = len(Q)
            for _ in range(cur_len):
                cur_path = Q.pop(0)
                last_w = cur_path[-1]
                visited.add(last_w)  # 经典之处！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                if last_w == endWord:
                    res.append(cur_path[:])
                else:
                    for i in range(m):
                        for nxt in bucket[last_w[:i] + '*' + last_w[i + 1:]]:
                            if nxt not in visited:
                                Q.append(cur_path[:] + [nxt])
            if res:
                return res[0]
        return []


class Solution:
    def check_translate(self, a: str, b: str) -> bool:  # 是否恰好有1位不同
        if len(a) != len(b):
            return False
        n = len(a)
        cnt = 0
        for i in range(n):
            if a[i] != b[i]:
                cnt += 1
        return cnt == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        adj_tbl = defaultdict(list)
        wordList.insert(0, beginWord)
        n = len(wordList)
        for i in range(n):
            for j in range(i+1,n):
                s, t = wordList[i], wordList[j]
                if self.check_translate(s,t):
                    adj_tbl[s].append(t)
                    adj_tbl[t].append(s)
        res = []
        q = [[beginWord]]
        visited = set()
        while q:
            for _ in range(len(q)):
                cur_path = q.pop(0)
                last_word = cur_path[-1]
                visited.add(last_word)
                if last_word==endWord:
                    res.append(cur_path[:])
                else:
                    for next_word in adj_tbl[last_word]:
                        if next_word not in visited:
                            q.append(cur_path[:]+[next_word])
            if res:
                return res[0]
        return []


if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    ret = sol.findLadders(beginWord, endWord, wordList)
    print(ret)
