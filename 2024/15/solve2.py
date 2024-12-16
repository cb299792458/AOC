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

def build_push_stack(r, c, d, stack):
    stack.append((r,c,d))

    nr, nc = r + dirs[d][0], c + dirs[d][1]

    if d in ['<', '>']:
        if grid[nr][nc] in ['[', ']']:
            build_push_stack(nr, nc, d, stack)
        return

    if grid[nr][nc] == '[':
        if grid[r][c] == '@' or grid[r][c] == ']':
            build_push_stack(nr, nc+1, d, stack)
        build_push_stack(nr, nc, d, stack)
    elif grid[nr][nc] == ']':
        if grid[r][c] == '@' or grid[r][c] == '[':
            build_push_stack(nr, nc-1, d, stack)
        build_push_stack(nr, nc, d, stack)
    
r,c = -1,-1
for i in range(M):
    for j in range(N):
        if grid[i][j] == '@':
            r,c = i,j

"""
This is some jank because I couldn't get the push stack/queue in the right order.
The boxes need to be pushed from the farthest to the closest, so that a piece of a
box never swaps with another piece of a box, only empty space.

I should have built the stack with level order traversal/bfs.
"""
sort_fns = {
    U: lambda x: -x[0],
    D: lambda x: x[0],
    L: lambda x: -x[1],
    R: lambda x: x[1]
}

for i in instructions:

    if can_move(r, c, i):
        stack = []
        build_push_stack(r, c, i, stack)

        new_stack = []
        seen = set()
        for t in stack:
            if t not in seen:
                seen.add(t)
                new_stack.append(t)
        stack = new_stack
        stack.sort(key=sort_fns[i])       

        while stack:
            (r, c, d) = stack.pop()
            swap(r,c,r+dirs[d][0],c+dirs[d][1])

        r += dirs[i][0]
        c += dirs[i][1]
        
for line in grid:
    print(''.join(line))
print()

gps = 0
for r in range(M):
    for c in range(N):
        if grid[r][c] == '[':
            gps += 100*r + c
print(gps)
