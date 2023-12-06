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
print(product)

# part 2
times = input[0].split()[1:]
dists = input[1].split()[1:]
time = int(''.join(times))
dist = int(''.join(dists))
def check(n):
    return (n*(time-n))>dist

def get_min():
    l,r = 0,time//2 # left bad, right good
    while l<r:
        m = l + (r-l)//2 # round down
        if check(m):
            r=m # if round up when m is good, inf loop
        else:
            l=m+1
    return r # return right

def get_max():
    l,r = time//2,time # left good, right bad
    while l<r:
        m = l + (1+r-l)//2 # round up
        if check(m):
            l=m # if round down, m = l (good), inf loop
        else:
            r=m-1
    return l


print(get_max()-get_min()+1)
