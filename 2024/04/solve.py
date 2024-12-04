input = [l[:-1] for l in open('input.txt','r').readlines()]
input = [list(line) for line in input]

M, N = len(input), len(input[0])
def get(r,c):
    if r < 0 or r >= M or c < 0 or c >= N:
        return '.'
    return input[r][c]

xmases = 0
for row in range(M):
    for col in range(N):
        [u, d, l, r, ul, ur, dl, dr] = ['', '', '', '', '', '', '', '']
        for i in range(4):
            u += get(row-i,col)
            d += get(row+i,col)
            l += get(row,col-i)
            r += get(row,col+i)
            ul += get(row-i,col-i)
            ur += get(row-i,col+i)
            dl += get(row+i,col-i)
            dr += get(row+i,col+i)
        strings = [u, d, l, r, ul, ur, dl, dr]
        xmases += len([s for s in strings if 'XMAS' == s])
print(xmases)

xmases = 0 

for r in range(M):
    for c in range(N):
        if get(r,c) != 'A':
            continue
        if (get(r-1,c-1) == 'M' and get(r+1,c+1) == 'S') or (get(r-1,c-1) == 'S' and get(r+1,c+1) == 'M'):
            if (get(r-1,c+1) == 'M' and get(r+1,c-1) == 'S') or (get(r-1,c+1) == 'S' and get(r+1,c-1) == 'M'):
                xmases += 1
print(xmases)
