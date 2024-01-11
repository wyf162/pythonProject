import sys

sys.stdout = open('./input.txt', 'w')
print(120, 50)
print(' '.join(map(str, [1] * 120)))
print(' '.join(map(str, [1]*10+[2]*20+[3]*10+[4]*10)))