import sys

sys.stdin = open('./input.txt')

N = 201
ans = 0
for _ in range(N):
    s = input()
    _, s = s.split(':')
    s1, s2 = s.split('|')
    win_numbers = [int(x) for x in s1.strip().replace('  ', ' ').split(' ')]
    numbers = [int(x) for x in s2.strip().replace('  ', ' ').split(' ')]
    c = 0
    for num in numbers:
        if num in win_numbers:
            c += 1
    print(c)
    if c:
        ans += 1 << (c - 1)
print(ans)
