import math
input = [l[:-1] for l in open('input.txt','r').readlines()]

def fewest_tokens(ax, ay, bx, by, xt, yt):
    res = math.inf
    for a in range(101):
        b = (xt - (a * ax)) // bx
        if -1 < b < 101 and (a*ax)+(b*bx) == xt and (a*ay)+(b*by) == yt:
            res = min(res, 3*a+b)
    
    return res if res < math.inf else 0

ans = 0

for i in range(0,len(input),4):
    line = input[i]
    [_, _, ax, ay] = line.split(' ')
    ax = int(ax[2:-1])
    ay = int(ay[2:])

    [_, _, bx, by] = input[i+1].split(' ')
    bx = int(bx[2:-1])
    by = int(by[2:])

    [_, xt, yt] = input[i+2].split(' ')
    xt = int(xt[2:-1])
    yt = int(yt[2:])

    ans += fewest_tokens(ax, ay, bx, by, xt, yt)

print(ans)
