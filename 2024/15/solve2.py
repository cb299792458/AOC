from collections import deque

input = open('input.txt','r').read().strip()
[layout, instructions] = input.split('\n\n')

grid = []
for line in layout.split('\n'):
    new_line = []
    for char in line:
        match char:
            case '#':
                new_line.append('#')
                new_line.append('#')
            case '.':
                new_line.append('.')
                new_line.append('.')

            case '@':
                new_line.append('@')
                new_line.append('.')
            case 'O':
                new_line.append('[')
                new_line.append(']')
    grid.append(new_line)

instructions = [c for c in instructions if c != '\n']

M, N = len(grid), len(grid[0])
U, D, L, R = '^', 'v', '<', '>'
dirs = {
    U: (-1, 0),
    D: (1, 0),
    L: (0, -1),
    R: (0, 1)
}

def swap(r,c,nr,nc):
    if grid[nr][nc] == '#':
        return
    grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]

def can_move(r, c, d):
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    if grid[nr][nc] == '#':
        return False
    if grid[nr][nc] == '.':
        return True
    
    assert grid[nr][nc] in ['[', ']']
    if d in ['<', '>']:
        return can_move(nr, nc, d)
    else:
        assert d in ['^', 'v']
        if grid[nr][nc] == '[':
            return can_move(nr, nc, d) and can_move(nr, nc+1, d)
        if grid[nr][nc] == ']':
            return can_move(nr, nc, d) and can_move(nr, nc-1, d)
        
    raise Exception('unknown character', r, c, d, grid[nr][nc])

def build_push_stack(r1, c1, d):
    queue = deque([(r1,c1)])
    seen = set()
    stack = []

    while queue:
        (r, c) = queue.popleft()
        if grid[r][c] == '.':
            continue
        if (r,c) in seen:
            continue
        seen.add((r,c))
        stack.append((r,c))

        nr, nc = r + dirs[d][0], c + dirs[d][1]
        queue.append((nr,nc))
        if grid[nr][nc] == '[':
            queue.append((nr,nc+1))
        if grid[nr][nc] == ']':
            queue.append((nr,nc-1))
    
    return stack

r,c = -1,-1
for i in range(M):
    for j in range(N):
        if grid[i][j] == '@':
            r,c = i,j

for d in instructions:

    if can_move(r, c, d):  
        stack = build_push_stack(r, c, d)

        while stack:
            (r, c) = stack.pop()
            swap(r,c,r+dirs[d][0],c+dirs[d][1])

        r += dirs[d][0]
        c += dirs[d][1]
        
for line in grid:
    print(''.join(line))
print()

gps = 0
for r in range(M):
    for c in range(N):
        if grid[r][c] == '[':
            gps += 100*r + c
print(gps)
