input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(l) for l in input]
M,N = len(grid),len(grid[0])

seen = set()
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def getAandP(r,c):
    if (r,c) in seen:
        return (0,0)
    seen.add((r,c))

    char = grid[r][c]

    a = 1
    p = 0

    for dr,dc in dirs:
        nr,nc = r+dr,c+dc
        if nr<0 or nc<0 or nr==M or nc==N or grid[nr][nc]!=char:
            p+=1
        else:
            (na,np) = getAandP(nr,nc)
            a+=na
            p+=np
    
    return (a,p)

# # part 1
# price = 0
# for r in range(M):
#     for c in range(N):
#         a,p = getAandP(r,c)
#         price += a*p
# print(price)
