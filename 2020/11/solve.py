input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in line] for line in input]
M, N = len(grid), len(grid[0])
dirs = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

def is_occupied(r, c):
    if r < 0 or r == M:
        return 0
    if c < 0 or c == N:
        return 0
    return 1 if grid[r][c] == '#' else 0

def count_neighbors(r, c):
    neighbors = 0
    for [dr, dc] in dirs:
        [nr, nc] = [r + dr, c + dc]
        neighbors += is_occupied(nr, nc)
    return neighbors

moves = 0
while True:
    moves += 1
    new_grid = [['.' for _ in range(N)] for _ in range(M)]

    for r in range(M):
        for c in range(N):
            if grid[r][c] == 'L':
                if count_neighbors(r, c) == 0:
                    new_grid[r][c] = '#'
                else:
                    new_grid[r][c] = 'L'
            elif grid[r][c] == '#':
                if count_neighbors(r, c) >= 4:
                    new_grid[r][c] = 'L'
                else:
                    new_grid[r][c] = '#'
    
    if grid == new_grid:
        break
    else:
        grid = new_grid

print(sum([len([c for c in line if c == '#']) for line in grid]))
