input = [l[:-1] for l in open('input.txt','r').readlines()]
input = [[c for c in l] for l in input]
# print(input)

ds = (-1, 0, 1)
N = 21

grid = [[[['.' for _ in range(N)] for __ in range(N)] for ___ in range(N)] for ____ in range(N)]

for x in range(len(input)):
    for y in range(len(input[0])):
        grid[N//2][N//2][x+N//3][y+N//3] = input[x][y]
# print(grid)

def neighbors(z, w, r, c):
    res = 0
    for dz in ds:
        for dw in ds:
            for dr in ds:
                for dc in ds:
                    if not -1 < z + dz < N:
                        continue
                    if not -1 < w + dw < N:
                        continue
                    if not -1 < r + dr < N:
                        continue
                    if not -1 < c + dc < N:
                        continue
                    if grid[z + dz][w+dw][r + dr][c + dc] == '#':
                        res += 1
    # print(res)
    return res

# def print_grid():
#     for z in range(N):
#         print(f'z={z}')
#         for row in grid[z]:
#             print(''.join(row))
# # print_grid()

def cycle():
    global grid
    new_grid = [[[['.' for _ in range(N)] for __ in range(N)] for ___ in range(N)] for ____ in range(N)]
    for z in range(N):
        for w in range(N):
            for r in range(N):
                for c in range(N):
                    n = neighbors(z, w, r, c)
                    if grid[z][w][r][c] == '#':
                        if n in (3, 4):
                            new_grid[z][w][r][c] = '#'
                    else:
                        if n == 3:
                            new_grid[z][w][r][c] = '#'
    grid = new_grid

for _ in range(6):
    cycle()

count = 0
for slice in grid:
    for idk in slice:
        for row in idk:
            for char in row:
                if char == '#':
                    count += 1
print(count)