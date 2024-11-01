from collections import deque

input = [l[:-1] for l in open('input.txt','r').readlines()][1:-1]
input = [list(line) for line in input]

A, B, C, D, E = "A", "B", "C", "D", "."
costs = {A: 1, B: 10, C: 100, D: 1000}
goals = {A: 3, B: 5, C: 7, D: 9}

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
    res = []
    for line in grid:
        for char in line:
            res.append(char)
        while len(res)%13!=0:
            res.append(' ')
    return ''.join(res)
def make_grid(key):
    return [list(key[i:i+13]) for i in range(0, len(key), 13)]

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
finished = "#...........####A#B#C#D###  #A#B#C#D#  "

# part 2
if len(input) > 3:
    finished = "#...........####A#B#C#D###  #A#B#C#D#    #A#B#C#D#    #A#B#C#D#  "

q = deque([(0, make_key(input))])
while q:
    (cost, key) = q.popleft()
    if key in seen:
        if cost<seen[key]:
            seen[key] = cost
        else:
            continue
    seen[key] = cost

    if cost>100000:
        continue
    if key == finished:
        continue
    if finished in seen and cost >= seen[finished]:
        continue

    grid = make_grid(key)

    for r1,c1 in rooms:
        if grid[r1][c1] == E:
            continue # no amphipod there to move
        char = grid[r1][c1]
        for r2,c2 in halls:
            if grid[r2][c2] != E:
                continue # target spot is not empty
            if not has_path((r1,c1),(r2,c2),grid):
                continue # cannot reach target spot

            must_move = False
            if c1 == goals[char]:
                for r in range(r1+1, len(grid)):
                    if grid[r][c1] != char:
                        must_move = True
            else:
                must_move = True
            if not must_move:
                continue # amphipod doesn't need to move

            dist = manhattan((r1,c1),(r2,c2))

            # move amphipod, enqueue next state, move it back
            grid[r1][c1] = E
            grid[r2][c2] = char
            q.append((cost + (costs[char] * dist), make_key(grid)))
            grid[r1][c1] = char
            grid[r2][c2] = E
    
    for r1,c1 in halls:
        if grid[r1][c1] == E:
            continue # no amphipod there to move
        char = grid[r1][c1]
        for r2,c2 in rooms:
            if grid[r2][c2] != E:
                continue # target spot is not empty
            if not has_path((r1,c1),(r2,c2),grid):
                continue # cannot reach target spot

            if goals[char] != c2:
                continue # not the right room for this amphipod

            occupied = False
            for r3 in range(r1+1, len(grid)):
                if grid[r3][c2] in [A,B,C,D] and grid[r3][c2]!=char:
                    occupied = True
                    break
            if occupied:
                continue # different amphipod in that room

            dist = manhattan((r1,c1),(r2,c2))

            # move amphipod, enqueue next state, move it back
            grid[r1][c1] = E
            grid[r2][c2] = char
            q.append((cost + (costs[char] * dist), make_key(grid)))
            grid[r1][c1] = char
            grid[r2][c2] = E

if finished in seen:
    print("solution:", seen[finished])
else:
    print("no solution found")
