input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

cave = [['.']*1000 for _ in range(172)]
# cave[0][500]='+'

for i in range(len(cave[0])):
    cave[171][i]='#'

ymax=0
for line in input:
    points = line.split(' -> ')
    prev = None
    for pt in points:
        coords = pt.split(',')
        cx,cy = int(coords[0]),int(coords[1])

        ymax=max(cy,ymax)
        if prev:
            px,py = prev
            cave[py][px] = '#'

            if py==cy:
                for x in range(min(px,cx),max(px,cx)+1):
                    cave[py][x]='#'
            else:
                for y in range(min(py,cy),max(py,cy)+1):
                    cave[y][px]='#'
        
        prev = cx,cy
# print(ymax)

def fall(i):
    pos = 0,500
    while True:
        x,y=pos
        # print(x,y,i)
        # if x>=171: return i
        if cave[x+1][y]=='.':
            pos = x+1,y
        elif cave[x+1][y-1]=='.':
            pos = x+1,y-1
        elif cave[x+1][y+1]=='.':
            pos = x+1,y+1
        else:
            cave[x][y]='o'
            return False


i=1
while True:
    if cave[0][500]=='.':
        fall(i)
        i+=1
    else:
        print(i)
        break

for row in cave:
    print(''.join(row)[400:600])
