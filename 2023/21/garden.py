input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in line] for line in input]
R,C = len(grid), len(grid[0])
dirs = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

S = (None,None)
for r in range(R):
    for c in range(C):
        if grid[r][c]=='S':
            S = (r,c)
# print(S)

odds_ = set([])
evens = set([S])

steps = 5000
for i in range(steps):
    starts = odds_ if i%2 else evens
    finals = evens if i%2 else odds_

    for (r,c) in starts:
        for d in dirs:
            nr, nc = r+d[0], c+d[1]
            if -1<nr<R and -1<nc<C and grid[nr][nc]!='#':
                finals.add((nr,nc))

print(len(finals))