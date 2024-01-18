import sys

if sys.platform.startswith('win'):
    sys.stdin = open('../everyday/input.txt', 'r')

n = input()
nums = list(map(int, input().split()))

max_inc = 0
max_dec = 0

inc = 0
dec = 0

for num in nums:
    x = 1 if num == 0 else -1
    inc = max(x, inc + x)
    max_inc = max(max_inc, inc)

    y = -1 if num == 0 else 1
    dec = max(y, dec + y)
    max_dec = max(dec, max_dec)

print(max_inc + max_dec + 1)

# s = 0
# ms = nums[0]
# for x in nums:
#     s = max(s+x, x)
#     ms = max(s, ms)
# return ms
