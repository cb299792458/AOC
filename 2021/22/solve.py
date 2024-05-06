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
    instructions.append([toggle=='on',x1,x2,y1,y2,z1,z2])

from collections import defaultdict
cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
for [toggle,x1,x2,y1,y2,z1,z2] in instructions:
    for x in range(int(x1),int(x2)+1):
        for y in range(int(y1),int(y2)+1):
            for z in range(int(z1),int(z2)+1):
                cubes[x][y][z] = toggle

trues = 0
for x in cubes:
    for y in cubes[x]:
        for z in cubes[x][y]:
            if cubes[x][y][z]:
                trues += 1
print(trues)
