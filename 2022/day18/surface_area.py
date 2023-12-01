input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

points = [(int(num) for num in line.split(',')) for line in input]
points = [tuple(l) for l in points]
# print(points)

dirs=(
    (1,0,0),
    (-1,0,0),
    (0,1,0),
    (0,-1,0),
    (0,0,1),
    (0,0,-1),
)

sa=0
cubes=set(points)
seen=set()

# part 1
sa=6*len(cubes)
for tup in points:
    for d in dirs:
        # check all 6 directions
        new=(tup[0]+d[0],tup[1]+d[1],tup[2]+d[2])

        if new in cubes: sa-=1
print(sa)


# part 2
osa=0
queue = [(0,0,0)]
while queue:
    curr=queue.pop(0)

    oob=False
    for c in curr:
        if c < -1 or c > 25: oob=True
    if oob: continue

    if curr in seen: continue
    seen.add(curr)

    for d in dirs:
        new=(curr[0]+d[0],curr[1]+d[1],curr[2]+d[2])
        if new in cubes:
            osa+=1
            continue
        else: 
            queue.append(new)

print(osa)