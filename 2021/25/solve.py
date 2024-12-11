input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in line] for line in input]
M, N = len(grid), len(grid[0])

def step(grid, i):
    copy = [row[:] for row in grid]
    
    moved = False
    for r in range(M):
        for c in range(N):
            if grid[r][c] != '>':
                continue
            if grid[r][(c+1)%N] == '.':
                copy[r][c], copy[r][(c+1)%N] = '.', '>'
                moved = True

    grid = copy
    copy = [row[:] for row in grid]
    
    for r in range(M):
        for c in range(N):
            if grid[r][c] != 'v':
                continue
            if grid[(r+1)%M][c] == '.':
                copy[r][c], copy[(r+1)%M][c] = '.', 'v'
                moved = True

    if not moved:
        print(i+1)
    return copy

for i in range(555):
    grid = step(grid, i)
