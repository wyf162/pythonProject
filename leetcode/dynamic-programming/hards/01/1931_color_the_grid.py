# _*_ coding: utf-8 _*_
# @Time : 2022/08/23 8:28 PM 
# @Author : yefe
# @File : 1931_color_the_grid

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        colors = ['r', 'g', 'b']
        states = []

        def dfs(state):
            if len(state) == m:
                states.append(state)
                return
            for color in colors:
                if state and color == state[-1]:
                    continue
                else:
                    dfs(state + color)

        dfs("")
        # print(states)
        # print(len(states))

        state_cnt = len(states)
        related = [[0] * state_cnt for _ in range(state_cnt)]
        for i in range(state_cnt):
            for j in range(state_cnt):
                if self.can_related(states[i], states[j]):
                    related[i][j] = 1

        f = [[0] * state_cnt for _ in range(n + 1)]
        f[1] = [1] * state_cnt

        for x in range(2, n + 1):
            for i in range(state_cnt):
                for j in range(state_cnt):
                    if related[i][j]:
                        f[x][i] += f[x - 1][j]
                        f[x][i] %= MOD

        return sum(f[-1]) % MOD

    @staticmethod
    def can_related(s1, s2):
        for x, y in zip(s1, s2):
            if x == y:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    m = 5
    n = 5
    ret = sol.colorTheGrid(m, n)
    print(ret)
