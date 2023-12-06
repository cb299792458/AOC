input = [l[:-1] for l in open('input.txt','r').readlines()]

# part 1
times = input[0].split()[1:]
dists = input[1].split()[1:]

times = [int(t) for t in times]
dists = [int(d) for d in dists]
product = 1
for time, dist in zip(times,dists):
    ways = 0
    for i in range(time):
        if i*(time-i)>dist:
            ways+=1
    product*=ways
# print(product)

# part 2
times = input[0].split()[1:]
dists = input[1].split()[1:]
time = int(''.join(times))
dist = int(''.join(dists))
print(time,dist)
def check(n):
    return (n*(time-n))>dist

import math
def get_min():
    l,r = 0,time
    while l<r:
        m = l + (r-l)//2
        if check(m):
            r=m
        else:
            l=m+1
    return r

def get_max():
    l,r = 0,time
    while l<r:
        m = l + (1+r-l)//2
        if check(m):
            l=m
        else:
            r=m-1
    return l


print(get_max()-get_min()+1)
