input = [l[:-1] for l in open('input.txt','r').readlines()]
R = len(input)
C = len(input[0])
start=None
for r,row in enumerate(input):
    for c, char in enumerate(row):
        if char=='S':
            start=(r,c)
print(start)

def N(pos):
    return (pos[0]-1,pos[1])
def S(pos):
    return (pos[0]+1,pos[1])
def E(pos):
    return (pos[0],pos[1]+1)
def W(pos):
    return (pos[0],pos[1]-1)
def get_p3(p1,p2):
    c = input[p2[0]][p2[1]]
    match c:
        case '-':
            if p2==E(p1):
                return E(p2)
            elif p2==W(p1):
                return W(p2)
        case '|':
            if p2==N(p1):
                return N(p2)
            elif p2==S(p1):
                return S(p2)
        case 'L':
            if p2==S(p1):
                return E(p2)
            elif p2==W(p1):
                return N(p2)
        case 'J':
            if p2==E(p1):
                return N(p2)
            elif p2==S(p1):
                return W(p2)
        case '7':
            if p2==N(p1):
                return W(p2)
            elif p2==E(p1):
                return S(p2)
        case 'F':
            if p2==N(p1):
                return E(p2)
            elif p2==W(p1):
                return S(p2)
        case _:
            print('uhoh')

path = [start, N(start)] # hardcode second step
while path[-1] != start:
    path.append(get_p3(path[-2],path[-1]))
# print(path)
# print(len(path))
print(len(path)//2)

ds = [(1,0),(-1,0),(0,1),(0,-1)]

def fill(aset,r,c):
    if (r,c) in aset:
        return
    if (r,c) in path_set:
        return
    if r<0 or c<0 or r==R or c==C:
        return
    
    aset.add((r,c))
    for d in ds:
        nr,nc = r+d[0],c+d[1]
        fill(aset,nr,nc)

set1 = set()
set2 = set()
path_set = set(path)

for i, pos in enumerate(path[:-1]):
    next_pos = path[i+1]
    c = input[pos[0]][pos[1]]

    if N(pos)==next_pos:
        # fill(set1,*W(pos))
        fill(set2,*E(pos))

        if c == 'J':
            fill(set2, *S(pos))        

    if E(pos)==next_pos:
        # fill(set1,*N(pos))
        fill(set2,*S(pos))

        if c=='L':
            fill(set2, *W(pos))

    if S(pos)==next_pos:
        # fill(set1,*E(pos))
        fill(set2,*W(pos))

        if c=='F':
            fill(set2, *N(pos))

    if W(pos)==next_pos:
        # fill(set1,*S(pos))
        fill(set2,*N(pos))

        if c=='7':
            fill(set2,*E(pos))

print(len(set1),len(set2))
