import copy

input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in line] for line in input]

M, N = len(grid), len(grid[0])
adjs = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)

def has_roll(r, c):
    if r < 0 or r == M or c < 0 or c == N:
        return False
    return grid[r][c] == '@'

def neighbors(r, c):
    count = 0
    for (dr, dc) in adjs:
        nr, nc = r + dr, c + dc
        if has_roll(nr, nc):
            count += 1
    return count

# # part 1
# accessible = 0
# for r in range(M):
#     for c in range(N):
#         if grid[r][c] == '@' and neighbors(r, c) < 4:
#             accessible += 1
# print(accessible)


# part 2
removed = 0
while True:
    new_grid = copy.deepcopy(grid)
    for r in range(M):
        for c in range(N):
            if grid[r][c] == '@' and neighbors(r, c) < 4:
                new_grid[r][c] = '.'
                removed += 1
    
    if grid == new_grid:
        break
    else:
        grid = new_grid

print(removed)
