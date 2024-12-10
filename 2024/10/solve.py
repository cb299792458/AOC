from collections import deque
from functools import cache
import time

input = [l[:-1] for l in open('input.txt','r').readlines()]

grid = [[int(c) for c in line] for line in input]
M, N = len(grid), len(grid[0])
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def count_reachable_nines(r,c):
    if grid[r][c] != 0:
        return 0

    seen = set()
    q = deque([(r,c,0)])

    while q:
        (cr, cc, ht) = q.popleft()

        if cr < 0 or cr >= M or cc < 0 or cc >= N:
            continue
        if grid[cr][cc] != ht:
            continue
        if (cr, cc, ht) in seen:
            continue
        seen.add((cr, cc, ht))

        q.append((cr+1, cc, ht+1))
        q.append((cr-1, cc, ht+1))
        q.append((cr, cc+1, ht+1))
        q.append((cr, cc-1, ht+1))
    
    return len([t for t in seen if t[2] == 9])

@cache
def count_paths_to_a_nine(r,c):
    if r<0 or r>=M or c<0 or c>=N:
        return 0
    if grid[r][c] == 9:
        return 1
    
    res = 0
    for d in dirs:
        (nr, nc) = (r+d[0], c+d[1])
        if nr<0 or nr>=M or nc<0 or nc>=N:
            continue
        if grid[nr][nc] == 1 + grid[r][c]:
            res += count_paths_to_a_nine(nr, nc)

    return res

start = time.time()

# part 1
score = 0

for r in range(M):
    for c in range(N):
        if grid[r][c] == 0:
            score += count_reachable_nines(r,c)

print(score)

# part 2
rating = 0
for r in range(M):
    for c in range(N):
        if grid[r][c] == 0:
            rating += count_paths_to_a_nine(r,c)

print(rating)

print(time.time()-start, 's')
