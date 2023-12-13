input = [l[:-1] for l in open('input.txt','r').readlines()]

grids = []
temp = []
for line in input:
    if line=='':
        grids.append(temp)
        temp = []
    else:
        temp.append(list(line))

# for grid in grids:
#     for line in grid:
#         print(''.join(line))
#     print('')

def is_reflected(grid, lines):
    for i in range(lines):
        if 2*lines-1-i >= len(grid):
            continue
        if grid[i]!=grid[2*lines-1-i]:
            return False
    return True

cols = dict()
rows = dict()

for g, grid in enumerate(grids):
    for i in range(1,len(grid)):
        if is_reflected(grid,i):
            rows[g] = i
    
    for i in range(1,len(grid[0])):
        if is_reflected(list(zip(*grid)),i):
            cols[g] = i

print(sum(cols.values())+100*sum(rows.values()))

new_h = []
new_r = []

for g, grid in enumerate(grids):
    R,C = len(grid), len(grid[0])
    for r in range(R):
        for c in range(C):
            grid[r][c] = '.' if grid[r][c]=='#' else '#'

            for i in range(1,len(grid)):
                if g in rows and rows[g]==i:
                    continue
                if is_reflected(grid,i):
                    new_r.append(i)
            
            for i in range(1,len(grid[0])):
                if g in cols and cols[g]==i:
                    continue
                if is_reflected(list(zip(*grid)),i):
                    new_h.append(i)
            
            grid[r][c] = '.' if grid[r][c]=='#' else '#'

print(100*sum(new_r)+sum(new_h))
# doubled nums in new_h and new_r, must divide by two
# BECAUSE THE SMUDGE AND ITS REFLECTION CAN BOTH BE CHANGED