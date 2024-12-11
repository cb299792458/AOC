"""
00a: append w + 14
01b: append w + 8
02c: append w + 5
03d: pop if w == z % 26 - 0
04e: append w + 10
05f: pop if w == z % 26 - 13
06g: append w + 16
07h: pop if w == z % 26 - 9
08i: append w + 6
09j: append w + 13
10k: pop if w == z % 26 - 14
11l: pop if w == z % 26 - 3
12m: pop if w == z % 26 - 2
13n: pop if w == z % 26 - 14

7 appends, need 7 pops

03: w[3] = w[2] + 5
05: w[5] = w[4] - 3
07: w[7] = w[6] + 16 - 9 = w[6] + 7
10: w[10] + 13 - 14 = w[10] = w[9] - 1
11: w[11] = w[8] + 6 - 3 = w[8] + 3
12: w[12] = w[1] + 8 - 2 = w[1] + 6
13: w[13] = w[0] + 14 - 14 = w[0]
"""
p1 = None
p2 = None

for a in range(1,10):
    n = a
    for b in range(1,10):
        m = b + 6
        if m<1 or m>9:
            continue
        for c in range(1,10):
            d = c + 5
            if d<1 or d>9:
                continue
            for e in range(1,10):
                f = e - 3
                if f<1 or f>9:
                    continue
                for g in range(1,10):
                    h = g + 7
                    if h<1 or h>9:
                        continue
                    for i in range(1,10):
                        l = i + 3
                        if l<1 or l>9:
                            continue
                        for j in range(1,10):
                            k = j - 1
                            if k<1 or k>9:
                                continue
                            num = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
                            if not p1:
                                p1 = num
                            p2 = num

print(''.join(map(str,p1)))
print(''.join(map(str,p2)))
