from collections import deque

input = [l[:-1] for l in open('input.txt','r').readlines()][1:-1]
input = [list(line) for line in input]
# for line in input:
#     print(''.join(line))

A, B, C, D, E = "A", "B", "C", "D", "."
costs = {A: 1, B: 10, C: 100, D: 1000}

halls = []
rooms = []
for r, row in enumerate(input):
    for c, char in enumerate(row):
        if char == '.':
            if c not in [3,5,7,9]:
                halls.append((r, c))
        elif char in [A, B, C, D]:
            rooms.append((r, c))

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def make_key(grid):
    return ''.join(''.join(line) for line in grid)
def make_grid(key):
    return [list(key[i:i+13]) for i in range(0, 39, 13)]

def has_path(t1,t2,grid):
    r1,c1 = t1
    r2,c2 = t2
    r,c = r1,c1

    if r1<r2:
        while c != c2:
            c += 1 if c2 > c1 else -1
            if grid[r][c]!=E and c!=c1:
                return False

        while r != r2:
            r += 1 if r2 > r1 else -1
            if grid[r][c]!=E and r!=r1:
                return False
    else:
        while r != r2:
            r += 1 if r2 > r1 else -1
            if grid[r][c]!=E and r!=r1:
                return False
        while c != c2:
            c += 1 if c2 > c1 else -1
            if grid[r][c]!=E and c!=c1:
                return False
    return True

seen = dict()
# burrows = copy.deepcopy(input)
# grid = make_grid(make_key(burrows))
finished = "#...........####A#B#C#D###  #A#B#C#D#"

q = deque([(0, make_key(input))])
while q:
    (cost, key) = q.popleft()
    if key in seen:
        if cost<seen[key]:
            seen[key] = cost
        else:
            continue
    seen[key] = cost
    
    if key == finished:
        continue
    if finished in seen and cost >= seen[finished]:
        continue

    grid = make_grid(key)
    for r1,c1 in rooms:
        if grid[r1][c1] == E:
            continue
        char = grid[r1][c1]
        for r2,c2 in halls:
            if grid[r2][c2] != E:
                continue
            if not has_path((r1,c1),(r2,c2),grid):
                continue

            dist = manhattan((r1,c1),(r2,c2))

            grid[r1][c1] = E
            grid[r2][c2] = char
            q.append((cost + (costs[char] * dist), make_key(grid)))
            grid[r1][c1] = char
            grid[r2][c2] = E
    
    for r1,c1 in halls:
        if grid[r1][c1] == E:
            continue
        char = grid[r1][c1]
        for r2,c2 in rooms:
            if grid[r2][c2] != E:
                continue
            if not has_path((r1,c1),(r2,c2),grid):
                continue

            if char==A and c2!=3:
                continue
            if char==B and c2!=5:
                continue
            if char==C and c2!=7:
                continue
            if char==D and c2!=9:
                continue

            if r2>0 and grid[r2-1][c2] in [A,B,C,D] and grid[r2-1][c2]!=char:
                continue
            if r2<2 and grid[r2+1][c2] in [A,B,C,D] and grid[r2+1][c2]!=char:
                continue

            dist = manhattan((r1,c1),(r2,c2))

            grid[r1][c1] = E
            grid[r2][c2] = char
            q.append((cost + (costs[char] * dist), make_key(grid)))
            grid[r1][c1] = char
            grid[r2][c2] = E
print(seen[finished])
