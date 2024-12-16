import heapq

input = [l[:-1] for l in open('input.txt','r').readlines()]

grid = [list(line) for line in input]
M, N = len(grid), len(grid[0])
S = (M-2, 1)
E = (1, N-2)
U, D, R, L = 'U', 'D', 'R', 'L'
dirs = {
    U: (-1, 0),
    D: (1, 0),
    R: (0, 1),
    L: (0, -1)
}

seen = dict()
q = [(0, R, *S, [])]
best = 10**20
paths = []

while q:
    (score, d, r, c, path) = heapq.heappop(q)
    path.append((r,c))

    if score > best:
        continue

    if grid[r][c] == '#':
        continue

    if (r, c) == E:
        best = min(best, score)
        print('reached the end with a score:', best)
        paths.append(path)
        continue

    if (d,r,c) in seen:
        if score > seen[(d,r,c)]:
            continue
    seen[(d,r,c)] = score

    heapq.heappush(q, (score+1, d, r+dirs[d][0], c+dirs[d][1], path.copy()))
    if d in [U,D]:
        heapq.heappush(q, (score+1000, L, r, c, path.copy()))
        heapq.heappush(q, (score+1000, R, r, c, path.copy()))
    else:
        heapq.heappush(q, (score+1000, U, r, c, path.copy()))
        heapq.heappush(q, (score+1000, D, r, c, path.copy()))

tiles = set()
for path in paths:
    for (r,c) in path:
        tiles.add((r,c))
print(len(tiles), 'tiles on any best path')
