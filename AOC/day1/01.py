import sys

sys.stdin = open('./input.txt')

rst = 0
for _ in range(1000):
    s = input()
    n = len(s)
    nums = []
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(n):
        if '0' <= s[i] <= '9':
            nums.append(int(s[i]))
        else:
            for j, digit in enumerate(digits, start=1):
                if s[i:i + len(digit)] == digit:
                    nums.append(j)
    rst += nums[0] * 10 + nums[-1]
    print(nums[0] * 10 + nums[-1])
print(rst)
