input = [l[:-1] for l in open('input.txt','r').readlines()]
U,D,L,R = 'U','D','L','R'
dirs = {
    U: (-1,0),
    D: (1,0),
    L: (0,-1),
    R: (0,1)
}

# # part 1
# r,c=0,0
# trench = set([(0,0)])
# for line in input:
#     [d,n,_] = line.split()
#     for _ in range(int(n)):
#         r,c = r+dirs[d][0], c+dirs[d][1]
#         trench.add((r,c))

# stack = [(-1,-1)]

# while stack:
#     (r,c) = stack.pop()
#     if (r,c) in trench:
#         continue
#     trench.add((r,c))

#     for d in dirs.values():
#         stack.append((r+d[0],c+d[1]))

# print(len(trench))

# part 2
area = 0
y=0

for line in input:
    (_,_,color) = line.split()
    dir = [R,D,L,U][int(color[-2])]
    num = int(color[2:-2],16)

    if dir==R:
        area += y*num # inner area
        area += num # perimeter
    if dir==L:
        area -= y*num # skip perimeter, inside area
    if dir==U:
        y += num
        area += num # include perimeter
    if dir==D:
        y -= num
area += 1 # perimeter of starting point
print(area)
