from collections import deque
input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(line) for line in input]
# print(grid)

ROWS, COLS = len(grid), len(grid[0])
U,D,L,R = 'U','D','L','R'
dirs = {
    U: (-1,0),
    D: (1,0),
    L: (0,-1),
    R: (0,1)
}

best = 0

def test(start):

    lit = set() #(row, col, dir)
    q = deque([start])

    while q:
        (r,c,d) = q.popleft() #(row, col, dir)
        if r<0 or c<0 or r==ROWS or c==COLS:
            continue
        if (r,c,d) in lit:
            continue
        lit.add((r,c,d))

        char = grid[r][c]
        match char:
            case '.':
                q.append((r+dirs[d][0],c+dirs[d][1],d))
            case '-':
                if d==L or d==R:
                    q.append((r+dirs[d][0],c+dirs[d][1],d))
                else:
                    q.append((r+dirs[L][0],c+dirs[L][1],L))
                    q.append((r+dirs[R][0],c+dirs[R][1],R))
            case '|':
                if d==U or d==D:
                    q.append((r+dirs[d][0],c+dirs[d][1],d))
                else:
                    q.append((r+dirs[U][0],c+dirs[U][1],U))
                    q.append((r+dirs[D][0],c+dirs[D][1],D))
            case '/':
                new_d = {U: R, R: U, L: D, D: L}[d]
                q.append((r+dirs[new_d][0],c+dirs[new_d][1],new_d))
            case '\\':
                new_d = {U: L, L: U, R: D, D: R}[d]
                q.append((r+dirs[new_d][0],c+dirs[new_d][1],new_d))

    energized = set()
    for (r,c,_) in lit:
        energized.add((r,c))

    global best
    best = max(best, len(energized))
    # print(len(energized))

# part 1
test((0,0,R))

# part 2
for r in range(ROWS):
    test((r,0,R))
    test((r,COLS-1,L))
for c in range(COLS):
    test((0,c,D))
    test((ROWS-1,c,U))
print(best)