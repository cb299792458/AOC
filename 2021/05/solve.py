input = [l[:-1] for l in open('input.txt','r').readlines()]

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in input:
    start, final = line.split(' -> ')
    c1,r1 = start.split(',')
    c2,r2 = final.split(',')
    (r1,c1,r2,c2) = (int(x) for x in (r1,c1,r2,c2))

    # if r1==r2:
    #     d = 1 if c1<c2 else -1
    #     for c in range(c1,c2+d,d):
    #         grid[r1][c]+=1
    # if c1==c2:
    #     d = 1 if r1<r2 else -1
    #     for r in range(r1,r2+d,d):
    #         grid[r][c1]+=1
    dr = 1 if r1<r2 else 0 if r1==r2 else -1
    dc = 1 if c1<c2 else 0 if c1==c2 else -1
    for i in range(max(abs(r2-r1),abs(c2-c1))+1):
        grid[r1+(i*dr)][c1+(i*dc)] += 1

points = 0
for row in grid:
    for num in row:
        if num>1:
            points+=1

print(points)