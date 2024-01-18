input()
S = list(input())
Q = int(input())
query = [input().split() for _ in range(Q)]
last = -1
for i, (t, _, _) in enumerate(query):
    if t == "2" or t == "3":
        last = i

for i, (t, x, c) in enumerate(query):
    if t == "1":
        S[int(x) - 1] = c
    elif t == "2":
        if i == last:
            S = list("".join(S).lower())
    else:
        if i == last:
            S = list("".join(S).upper())

print("".join(S))




