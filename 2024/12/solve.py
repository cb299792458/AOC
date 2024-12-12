input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(l) for l in input]
M,N = len(grid),len(grid[0])

seen = set()
# dirs = [(0,1),(1,0),(0,-1),(-1,0)]
U,D,L,R = 'U', 'D', 'L', 'R'
dirs = {
    U: (-1,0),
    D: (1,0),
    L: (0,-1),
    R: (0,1)
}

def getAandP(r,c):
    if (r,c) in seen:
        return (0,0)
    seen.add((r,c))

    char = grid[r][c]

    a = 1
    p = 0

    for dr,dc in dirs.values():
        nr,nc = r+dr,c+dc
        if nr<0 or nc<0 or nr==M or nc==N or grid[nr][nc]!=char:
            p+=1
        else:
            (na,np) = getAandP(nr,nc)
            a+=na
            p+=np
    
    return (a,p)

def fill_region(r, c, char, curr):
    if (r,c) in seen:
        return
    if r<0 or c<0 or r==M or c==N:
        return
    if grid[r][c] != char:
        return

    seen.add((r,c))
    curr.add((r,c))

    for (dr,dc) in dirs.values():
        fill_region(r+dr,c+dc,char,curr)
    
    return curr

def get_borders_from_region(region):
    borders = set()
    for (r,c) in region:
        for [d, (dr,dc)] in dirs.items():
            nr,nc = r+dr,c+dc
            if (nr,nc) not in region:
                borders.add((r,c,d))
    return borders

def count_sides_from_borders(borders):
    borders = sorted(borders)
    sides = 0
    seen = set()

    for (r,c,d) in borders:
        match d:
            case 'U':
                if (r,c+1,U) not in seen and (r,c-1,U) not in seen:
                    sides += 1
            case 'D':
                if (r,c+1,D) not in seen and (r,c-1,D) not in seen:
                    sides += 1
            case 'L':
                if (r+1,c,L) not in seen and (r-1,c,L) not in seen:
                    sides += 1
            case 'R':
                if (r+1,c,R) not in seen and (r-1,c,R) not in seen:
                    sides += 1
        seen.add((r,c,d))

    return sides



# # part 1
# price = 0
# for r in range(M):
#     for c in range(N):
#         a,p = getAandP(r,c)
#         price += a*p
# print(price)

# part 2
regions = []

for r in range(M):
    for c in range(N):
        region = fill_region(r, c, grid[r][c], set())
        if region:
            regions.append(region)

price = 0
for region in regions:
    borders = get_borders_from_region(region)
    sides = count_sides_from_borders(borders)
    price += sides * len(region)
print(price)
