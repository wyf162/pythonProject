import sys

# sys.stdin = open('./../input.txt', 'r')
s = input()

cnt = 0
ans = ''
for c in s:
    if c == '1':
        cnt += 1
    else:
        ans += c

pos = -1
while pos + 1 < len(ans) and ans[pos + 1] == '0':
    pos += 1
ans = ans[:pos+1] + '1' * cnt + ans[pos+1:]
print(ans)
