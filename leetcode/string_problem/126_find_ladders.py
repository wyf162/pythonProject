# _*_ coding: utf-8 _*_
# @Time : 2022/4/9 下午10:04 
# @Author : wangyefei
# @File : 126_find_ladders.py
from collections import defaultdict
from typing import List
from collections import deque
import string


class Solution2:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表

        found = self.__bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True

                                # 避免下层元素重复加入队列
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)

                                successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 事实上是有的，毫无疑问我是撸舍
        wordList2Set = set(wordList)
        if endWord not in wordList2Set:
            return []
        res = []
        from collections import deque
        q = deque([[beginWord, [beginWord]]])
        visited = set()

        while q:
            new_visited = set()
            for _ in range(len(q)):
                cur_word, cur_path = q.popleft()
                for i in range(len(cur_word)):
                    for j in range(26):
                        tmp = cur_word[:i] + chr(ord('a') + j) + cur_word[i + 1:]
                        if tmp not in visited and tmp in wordList2Set:
                            new_visited.add(tmp)
                            q.append([tmp, cur_path + [tmp]])
                            if tmp == endWord:
                                res.append(cur_path + [tmp])
            visited |= new_visited
            if res:
                return res
        return res