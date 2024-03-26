# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

s = input()
n = len(s)
left, ans = 0, 0
for i in range(n):
    if s[i] == ')' and left:
        ans += 2
        left -= 1
    elif s[i] == '(':
        left += 1
print(ans)
