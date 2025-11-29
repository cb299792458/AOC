input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in line] for line in input]
M, N = len(grid), len(grid[0])


def count_trees(right, down):
    r, c, trees = 0, 0, 0

    while r < M:
        if grid[r][c%N] == '#':
            trees += 1
        r += down
        c += right

    print(trees)
    return trees

opts = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]
res = 1

for [right, down] in opts:
    res *= count_trees(right, down)
print(res)
