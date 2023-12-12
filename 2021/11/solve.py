input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[int(c) for c in line] for line in input]
dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

flashes = 0
def update():
    flashed = []
    new_flash = True
    while new_flash:
        new_flash = False
        for r in range(10):
            for c in range(10):
                if (r,c) not in flashed and grid[r][c]>9:
                    flashed.append((r,c))
                    global flashes
                    flashes += 1
                    new_flash = True

                    for dir in dirs:
                        nr,nc = r+dir[0],c+dir[1]
                        if nr<0 or nc<0 or nr==10 or nc==10:
                            continue
                        grid[nr][nc] += 1

def normalize():
    for r in range(10):
        for c in range(10):
            if grid[r][c]>9:
                grid[r][c] = 0

def check(i):
    res = True
    for r in range(10):
        for c in range(10):
            if grid[r][c]!=0:
                res = False
    if res:
        print(i+1)


for i in range(1000):
    for r in range(10):
        for c in range(10):
            grid[r][c]+=1
    update()
    normalize()
    check(i)

print(flashes)

