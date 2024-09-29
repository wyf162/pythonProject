
s = 'a'
s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = s1[1:] + s1[0]
hst = {c1: c2 for c1, c2 in zip(s1, s2)}
while len(s) < 505:
    t = ''
    for c in s:
        t += hst[c]
    s += t


class Solution:
    def kthCharacter(self, k: int) -> str:
        return s[k-1]


if __name__ == "__main__":
    sol = Solution()
    k = 10
    ret = sol.kthCharacter(k)
    print(ret)
