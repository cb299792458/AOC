import time
input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in l] for l in input]
M, N = len(grid), len(grid[0])

dirs = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]
di = 0
ri = ci = 0

for i in range(M):
    for j in range(N):
        if grid[i][j] not in ['.','#']:
            ri=i
            ci=j
r = ri
c = ci

seen = set()

while -1<r<M and -1<c<N:
    seen.add((r,c))
    nr, nc = r+dirs[di%4][0], c+dirs[di%4][1]
    if -1<nr<M and -1<nc<N and grid[nr][nc] == '#':
        di += 1
    else:
        r, c = nr, nc

print(len(seen))

# part 2
loops = 0

def add_obstacle(ro,co):
    global grid, M, N
    if grid[ro][co] == '.':
        grid[ro][co] = '#'
    else:
        return False
    
    seen = set()
    r = ri
    c = ci
    di = 0

    while -1<r<M and -1<c<N:
        if (r,c,di%4) in seen:
            grid[ro][co] = '.'
            return True
        seen.add((r,c,di%4))

        nr, nc = r+dirs[di%4][0], c+dirs[di%4][1]
        if -1<nr<M and -1<nc<N and grid[nr][nc] == '#':
            di += 1
        else:
            r, c = nr, nc
    
    grid[ro][co] = '.'
    return False

t = time.time()
for r in range(M):
    for c in range(N):
        if add_obstacle(r,c):
            loops += 1
print(loops)
print(time.time()-t)
