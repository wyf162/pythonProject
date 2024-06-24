import sys

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
queries = [LI() for _ in range(n)]


def get_max_prefix(a, b):
    s, t = bin(a)[2:], bin(b)[2:]
    ans = 0
    if len(s) == len(t):
        for i in range(0, len(s)):
            if s[i] == t[i]:
                if s[i] == '1':
                    ans |= (1 << (len(s) - i-1))
            else:
                break
    return ans


for l, r in queries:
    prefix = get_max_prefix(l, r)
    y = r - prefix
    x = 0
    for i in range(64):
        if x | (1 << i) <= y:
            x |= (1 << i)
        else:
            break
    ans = prefix + x
    print(ans)
