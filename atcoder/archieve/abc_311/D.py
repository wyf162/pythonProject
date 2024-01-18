N, M = map(int, input().split())
S = [input() for _ in range(N)]

seen = [[False] * M for _ in range(N)]
seen[1][1] = True
stack = [[1, 1]]
visited = {(1, 1)}
while len(stack) > 0:
    y, x = stack.pop()
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y, x
        while ((0 <= ny + dy < N) and (0 <= nx + dx < M)) and (S[ny + dy][nx + dx] == "."):
            ny += dy
            nx += dx
            seen[ny][nx] = True
        if (ny, nx) not in visited:
            visited.add((ny, nx))
            stack.append((ny, nx))

ans = sum(sum(line) for line in seen)
print(ans)
