input = [l[:-1] for l in open('input.txt','r').readlines()]
from collections import deque
R,C = len(input), len(input[0])

def height(r,c):
    if r<0 or c<0 or r==R or c==C:
        return 9
    return int(input[r][c])

risks = 0
lows = []
for r in range(R):
    for c in range(C):
        h = height(r,c)
        if h<height(r+1,c) and h<height(r-1,c) and h<height(r,c+1) and h<height(r,c-1):
            lows.append((r,c))
            risks+=h+1
print(risks)

basins = []
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
for low in lows:
    q = deque([low])
    basin = set()

    while q:
        tup = q.popleft()
        if tup in basin:
            continue
        basin.add(tup)

        r,c = tup
        h = height(r,c)
        for dir in dirs:
            nr,nc = r+dir[0], c+dir[1]
            nh = height(nr,nc)
            if h<nh<9:
                q.append((nr,nc))
    basins.append(list(basin))

basins.sort(key=lambda b: len(b))
for b in basins[-3:]:
    print(len(b))