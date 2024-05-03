input = [l[:-1] for l in open('input.txt','r').readlines()]

p1 = 1
p2 = 3
s1 = 0
s2 = 0
die = 0
rolls = 0

while s1<1000 and s2<1000:
    for _ in range(3):
        die += 1
        p1 += die
        while p1>10:
            p1 -= 10
        rolls += 1
        if die>=100: die = 0
    s1 += p1
    if s1 >= 1000:
        print(s1,s2,rolls)


    for _ in range(3):
        die += 1
        p2 += die
        while p2>10:
            p2 -= 10
        rolls += 1
        if die>=100: die  = 0
    s2 += p2
    if s2>= 1000:
        print(s1,s2,rolls)

