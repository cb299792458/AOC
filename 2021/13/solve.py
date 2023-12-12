input = [l[:-1] for l in open('input.txt','r').readlines()]

# maxr,maxc=0,0
# for line in input[:866]:
#     r,c = line.split(',')
#     r,c = int(r),int(c)
#     maxr=max(maxr,r)
#     maxc=max(maxc,c)
# print(maxr,maxc)

grid = [[' ' for _ in range(900)] for _ in range(1400)]

for line in input[:866]:
    r,c = line.split(',')
    r,c = int(r),int(c)
    grid[r][c]='#'

    # if r > 655:
    #     nr = 655 + 655 - r
    #     grid[r][c]=' '
    #     grid[nr][c]='#'
    
# count = 0
# for row in grid:
#     for c in row:
#         if c=='#':
#             count+=1
# print(count)

for line in input[867:]:
    R,C = len(grid), len(grid[0])
    new_grid = [[' ' for _ in range(C)] for _ in range(R)]

    _,_,s = line.split()
    dim, num = s.split('=')
    num=int(num)

    for r in range(R):
        for c in range(C):
            if dim=='x' and r>num:
                nr = 2*num-r
                if grid[r][c]=='#':
                    new_grid[nr][c]='#'
            elif dim=='y' and c>num:
                nc = 2*num-c
                if grid[r][c]=='#':
                    new_grid[r][nc]='#'
            else:
                new_grid[r][c] = grid[r][c]
    grid = new_grid

grid = [row[:6] for row in grid]
grid = grid[:40]
grid = list(zip(*grid))

for line in grid:
    print(''.join(line))