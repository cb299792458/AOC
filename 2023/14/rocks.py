input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(line) for line in input]
R,C = len(grid), len(grid[0])

def north():
    for r in range(R):
        for c in range(C):
            if grid[r][c]=='O':
                temp_r = r
                while temp_r and grid[temp_r-1][c]=='.':
                    grid[temp_r-1][c]='O'
                    grid[temp_r][c]='.'
                    temp_r-=1

def south():
    for r in range(R-1,-1,-1):
        for c in range(C):
            if grid[r][c]=='O':
                temp_r = r
                while temp_r<R-1 and grid[temp_r+1][c]=='.':
                    grid[temp_r+1][c]='O'
                    grid[temp_r][c]='.'
                    temp_r+=1

def east():
    for c in range(C-1,-1,-1):
        for r in range(R):
            if grid[r][c]=='O':
                temp_c = c
                while temp_c<C-1 and grid[r][temp_c+1]=='.':
                    grid[r][temp_c+1]='O'
                    grid[r][temp_c]='.'
                    temp_c+=1

def west():
    for c in range(C):
        for r in range(R):
            if grid[r][c]=='O':
                temp_c = c
                while temp_c and grid[r][temp_c-1]=='.':
                    grid[r][temp_c-1]='O'
                    grid[r][temp_c]='.'
                    temp_c-=1

def print_grid():
    for line in grid:
        print(''.join(line))
    print('')

def print_load():
    load = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c]=='O':
                load += R-r

    print(load)
    return load

# # part 1
# north()
# print_load()

# part 2
from collections import Counter
counts = Counter()
for _ in range(1000):
    north()
    west()
    south()
    east()
    counts[print_load()]+=1
# print(counts)
# print(len([val for val in counts.values() if val>30]))
cycle = len([val for val in counts.values() if val>30])
assert((1000000000 - 1000)%cycle == 0)