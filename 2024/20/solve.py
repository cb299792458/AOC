from collections import deque
input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(l) for l in input]
start, end = (), ()
M, N = len(grid), len(grid[0])
for r in range(M):
    for c in range(N):
        if grid[r][c] == 'S':
            start = (r, c)
        if grid[r][c] == 'E':
            end = (r, c)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

dist_to_start = dict()
queue = deque([(start, 0)])

while queue:
    ((r, c), picoseconds) = queue.popleft()
    if grid[r][c] == '#':
        continue
    if (r, c) in dist_to_start:
        continue
    dist_to_start[(r, c)] = picoseconds
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = r + dr, c + dc
        queue.append([(new_r, new_c), picoseconds + 1])

dist_to_end = dict()
queue = deque([(end, 0)])

while queue:
    ((r, c), picoseconds) = queue.popleft()
    if grid[r][c] == '#':
        continue
    if (r, c) in dist_to_end:
        continue
    dist_to_end[(r, c)] = picoseconds
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = r + dr, c + dc
        queue.append([(new_r, new_c), picoseconds + 1])

# part 1
cheats = 0
for [t1, d1] in dist_to_start.items():
    for [t2, d2] in dist_to_end.items():
        if manhattan(t1, t2) == 2:
            if dist_to_start[end] - d1 - d2 >= 100 + manhattan(t1, t2):
                cheats += 1
print(cheats)

# part 2
cheats = 0
for [t1, d1] in dist_to_start.items():
    for [t2, d2] in dist_to_end.items():
        if manhattan(t1, t2) <= 20:
            time = d1 + d2 + manhattan(t1, t2)
            if dist_to_start[end] - time >= 100:
                cheats += 1
print(cheats)
