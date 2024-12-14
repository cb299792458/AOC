input = [l[:-1] for l in open('input.txt','r').readlines()]

M=103
N=101
robots = []

for line in input:
    [p, v] = line.split(' ')
    px, py = p[2:].split(',')
    px, py = int(px), int(py)
    vx, vy = v[2:].split(',')
    vx, vy = int(vx), int(vy)
    robots.append({
        'px': px,
        'py': py,
        'vx': vx,
        'vy': vy
    })

tree = False
for i in range(50000):
    grid = [[' ' for _ in range(N)] for _ in range(M)]

    for r in robots:
        r['px'] += r['vx']
        r['py'] += r['vy']
        r['px'] %= N
        r['py'] %= M

        px = r['px']
        py = r['py']
        grid[py][px] = '#'

        if (
            -1<px<N-1 and -1<py<M-1 and
            grid[py-1][px] == '#' and
            grid[py+1][px] == '#' and
            grid[py][px-1] == '#' and
            grid[py][px+1] == '#' and
            grid[py-1][px-1] == '#' and
            grid[py+1][px+1] == '#' and
            grid[py-1][px+1] == '#' and
            grid[py+1][px-1] == '#'
        ):
            tree = True
    
    if tree:
        for row in grid:
            print(''.join(row))
        print(i+1)
        break

nw = 0
ne = 0
sw = 0
se = 0
for r in robots:
    px = r['px']
    py = r['py']

    if px < N//2 and py < M//2:
        nw += 1
    elif px < N//2 and py > M//2:
        sw += 1
    elif px > N//2 and py < M//2:
        ne += 1
    elif px > N//2 and py > M//2:
        se += 1

print(nw, ne, sw, se, nw*ne*sw*se)
