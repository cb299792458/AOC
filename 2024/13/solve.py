import math
input = [l[:-1] for l in open('input.txt','r').readlines()]

def fewest_tokens(ax, ay, bx, by, xt, yt):
    res = math.inf
    for a in range(101):
        b = (xt - (a * ax)) // bx
        if -1 < b < 101 and (a*ax)+(b*bx) == xt and (a*ay)+(b*by) == yt:
            res = min(res, 3*a+b)
    
    return res if res < math.inf else 0

def inv(matrix):
    [[a, b], [c, d]] = matrix
    det = a*d - b*c
    return [[d/det, -b/det], [-c/det, a/det]]

def mul(m1, m2):
    [[a, b], [c, d]] = m1
    [[x],[y]] = m2
    return [[a*x+b*y], [c*x+d*y]]

def count_tokens(a,b):
    round_a = round(a)
    round_b = round(b)
    if abs(a - round_a) < .001 and abs(b - round_b) < .001:
        return 3*round_a+round_b
    return 0

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

    # part 2
    xt += 10000000000000
    yt += 10000000000000

    [[a], [b]] = mul(inv([[ax, bx], [ay, by]]), [[xt], [yt]])
    ans += count_tokens(a,b)

print(ans)


