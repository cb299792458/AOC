input = open('input.txt','r').read().strip()
[grid, instructions] = input.split('\n\n')

grid = [list(line) for line in grid.split('\n')]
instructions = [c for c in instructions if c != '\n']

M, N = len(grid), len(grid[0])
U, D, L, R = '^', 'v', '<', '>'
dirs = {
    U: (-1, 0),
    D: (1, 0),
    L: (0, -1),
    R: (0, 1)
}

def swap(r,c,nr,nc):
    if grid[nr][nc] == '#':
        return
    grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]

r,c = -1,-1
for i in range(M):
    for j in range(N):
        if grid[i][j] == '@':
            r,c = i,j

for i in instructions:
    dr, dc = dirs[i]

    # part 1
    fr, fc = r, c
    while grid[fr][fc] not in ['#','.']:
        fr += dr
        fc += dc

    if grid[fr][fc] == '#':
        continue

    while (fr, fc) != (r, c):
        swap(fr, fc, fr - dr, fc - dc)
        fr -= dr
        fc -= dc
    
    r += dr
    c += dc

for line in grid:
    print(''.join(line))

gps = 0
for r in range(M):
    for c in range(N):
        if grid[r][c] == 'O':
            gps += 100*r + c
print(gps)
