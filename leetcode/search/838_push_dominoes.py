# _*_ coding: utf-8 _*_
# @Time : 2022/2/21 下午10:44 
# @Author : wangyefei
# @File : 838_push_dominoes.py

from collections import deque


class Solution:
    def push_dominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        unvisited = [True] * n
        ans = ['.'] * n
        for idx, domino in enumerate(dominoes):
            if domino != '.':
                q.append(idx)
                unvisited[idx] = False
                ans[idx] = domino
        while q:
            next_level = set()
            for _ in range(len(q)):
                i = q.popleft()
                state = ans[i]
                if state == 'L' and i - 1 >= 0 and unvisited[i - 1]:
                    q.append(i - 1)
                    next_level.add(i - 1)
                    ans[i - 1] = '.' if ans[i - 1] == 'R' else 'L'
                if state == 'R' and i + 1 < n and unvisited[i + 1]:
                    q.append(i + 1)
                    next_level.add(i + 1)
                    ans[i + 1] = '.' if ans[i + 1] == 'L' else 'R'
            for i in next_level:
                unvisited[i] = False
        return ''.join(ans)

    def push_dominoes_v2(self, dominoes: str) -> str:
        s = list(dominoes)
        n, i, left = len(s), 0, 'L'
        while i < n:
            j = i
            while j < n and s[j] == '.':
                j += 1
            right = s[j] if j < n else 'R'
            if left == right:
                while i < j:
                    s[i] = right
                    i += 1
            elif left == 'R' and right == 'L':
                k = j - 1
                while i < k:
                    s[i] = 'R'
                    s[k] = 'L'
                    i += 1
                    k -= 1
            left = right
            i = j + 1
        return ''.join(s)


if __name__ == '__main__':
    sol = Solution()
    # dominoes = ".L.R...LR..L.."
    # dominoes = "RR.L"
    # dominoes = ".L.R...LR..L.."
    dominoes = "..R.."
    ret = sol.push_dominoes_v2(dominoes)
    print(ret)
