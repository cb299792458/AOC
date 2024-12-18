input = [l[:-1] for l in open('input.txt','r').readlines()]
GRID_SIZE = 71
BYTES = 1024

grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

from collections import deque

def find_min_steps():
    queue = deque([(0,0,0)])
    visited = set()

    while queue:
        (steps, r, c) = queue.popleft()
        if r<0 or r>=GRID_SIZE or c<0 or c>=GRID_SIZE:
            continue
        if grid[r][c] == '#':
            continue
        if (r,c) in visited:
            continue
        visited.add((r,c))

        if r == GRID_SIZE-1 and c == GRID_SIZE-1:
            return steps

        queue.append((steps+1, r+1, c))
        queue.append((steps+1, r-1, c))
        queue.append((steps+1, r, c+1))
        queue.append((steps+1, r, c-1))

    return -1

# # part 1
# for i in range(BYTES):
#     [c, r] = input[i].split(',')
#     c = int(c)
#     r = int(r)
#     grid[r][c] = '#'
# print(find_min_steps())

# part 2
for [i, line] in enumerate(input):
    print(i)
    
    [c, r] = line.split(',')
    c = int(c)
    r = int(r)
    grid[r][c] = '#'
    if find_min_steps() == -1:
        print(f'[{c},{r}]')
        break
