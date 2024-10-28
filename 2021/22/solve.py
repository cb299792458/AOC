from collections import defaultdict, deque
input = [l[:-1] for l in open('input.txt','r').readlines()]

instructions = []
for line in input:
    [toggle, rest] = line.split(' ')
    [x,y,z] = rest.split(',')
    x = x[2:]
    y = y[2:]
    z = z[2:]
    [x1,x2] = x.split('..')
    [y1,y2] = y.split('..')
    [z1,z2] = z.split('..')
    instructions.append([toggle=='on',*list(map(int,[x1,x2,y1,y2,z1,z2]))])

def volume(x1,x2,y1,y2,z1,z2):
    if x1>x2 or y1>y2 or z1>z2:
        return 0
    return (x2-x1+1)*(y2-y1+1)*(z2-z1+1)

def overlap(x1, x2, y1, y2, z1, z2, u1, u2, v1, v2, w1, w2):
    # Calculate overlap bounds
    ox1, ox2 = max(x1, u1), min(x2, u2)
    oy1, oy2 = max(y1, v1), min(y2, v2)
    oz1, oz2 = max(z1, w1), min(z2, w2)
    
    # Ensure the overlap region has a positive volume in all dimensions
    if ox1 <= ox2 and oy1 <= oy2 and oz1 <= oz2:
        return [ox1, ox2, oy1, oy2, oz1, oz2]
    else:
        # Return None if there is no valid overlap
        return None

    

# part 1
cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
for [on,x1,x2,y1,y2,z1,z2] in instructions:
    ol = overlap(x1,x2,y1,y2,z1,z2,-50,50,-50,50,-50,50)
    if not ol:
        continue

    [x,X,y,Y,z,Z] = ol
    for i in range(x,X+1):
        for j in range(y,Y+1):
            for k in range(z,Z+1):
                cubes[i][j][k] = on
print(sum([cubes[i][j][k] for i in cubes for j in cubes[i] for k in cubes[i][j]]))

# part 2
on_cubes  = []
off_cubes = []

for [on,x1,x2,y1,y2,z1,z2] in instructions:
    new_ons = []
    new_off = []
    curr = [x1,x2,y1,y2,z1,z2]
    for prev in off_cubes:
        ol = overlap(*curr,*prev)
        if ol:
            new_ons.append(ol)
    for prev in on_cubes:
        ol = overlap(*curr,*prev)
        if ol:
            new_off.append(ol)
    if on:
        new_ons.append(curr)
    
    on_cubes.extend(new_ons)
    off_cubes.extend(new_off)

print(sum([volume(*c) for c in on_cubes]) - sum([volume(*c) for c in off_cubes]))
