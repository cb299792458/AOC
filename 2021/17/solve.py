input = [l[:-1] for l in open('input.txt','r').readlines()]

xmin,xmax,ymin,ymax = 59,95,-172,-135
# xmin,xmax,ymin,ymax = 19,31,-11,-4

count = 0

def shoot(vx,vy):
    orig = (vx,vy)
    x,y=0,0
    highest = 0
    while x<xmax and y>ymin:
        x+=vx
        y+=vy
        highest = max(highest, y)
        if vx: vx-=1
        vy-=1
        if xmin<x<xmax and ymin<y<ymax:
            global count
            count += 1
            # print('hit', orig, highest)
            break


for x in range(1,2000):
    for y in range(-300,600):
        shoot(x,y)
print(count)