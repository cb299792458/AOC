from collections import deque
input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
height = len(input)
width = len(input[0])
start = (0,1)
end = (height-1,width-2)
dirs = {
    '^': (-1,0),
    '>': (0,1),
    '<': (0,-1),
    'v': (1,0),
}

LCM = 12 #example least common multiple
LCM = 600 #actual

class Blizzard:
    def __init__(self,r,c,d) -> None:
        self.r = r
        self.c = c
        self.d = d

    def move(self):
        self.r += dirs[self.d][0]
        self.c += dirs[self.d][1]

        if self.r==0: self.r=height-2
        if self.r==height-1: self.r=1
        if self.c==0: self.c=width-2
        if self.c==width-1: self.c=1
blizzards=[]

for r in range(1,height-1):
    for c in range(1,width-1):
        if input[r][c]!='#' and input[r][c]!='.':
            blizzards.append(Blizzard(r,c,input[r][c]))

def move_all_blizzards():
    positions = set()
    for blizzard in blizzards:
        blizzard.move()
        positions.add((blizzard.r,blizzard.c))
    return positions

maps = [None]
for _ in range(LCM+1):
    maps.append(move_all_blizzards())
maps[0] = maps[LCM]

# trip 1
queue = deque([(0,start[0],start[1])])
seen = set()

while queue:
    (time, r, c) = queue.popleft()

    if (time%LCM,r,c) in seen: continue
    seen.add((time%LCM,r,c))
    # print(seen)

    if (r,c)==end:
        print(time)
        break

    time+=1

    map = maps[time%LCM]

    if (r,c) not in map:
        queue.append((time,r,c))

    for dir in dirs.values():
        (nr,nc) = (r+dir[0],c+dir[1])
        if (nr,nc) not in map and input[nr][nc] != '#':
            queue.append((time,nr,nc))

#trip 2
queue = deque([(286,end[0],end[1])])
seen = set()
while queue:
    (time, r, c) = queue.popleft()

    if (time%LCM,r,c) in seen: continue
    seen.add((time%LCM,r,c))
    # print(seen)

    if (r,c)==start:
        print(time)
        break

    time+=1

    map = maps[time%LCM]

    if (r,c) not in map:
        queue.append((time,r,c))

    for dir in dirs.values():
        (nr,nc) = (r+dir[0],c+dir[1])
        if (nr,nc) not in map and nr<height-1 and input[nr][nc] != '#':
            queue.append((time,nr,nc))

#trip 3
queue = deque([(541,start[0],start[1])])
seen = set()

while queue:
    (time, r, c) = queue.popleft()

    if (time%LCM,r,c) in seen: continue
    seen.add((time%LCM,r,c))
    # print(seen)

    if (r,c)==end:
        print(time)
        break

    time+=1

    map = maps[time%LCM]

    if (r,c) not in map:
        queue.append((time,r,c))

    for dir in dirs.values():
        (nr,nc) = (r+dir[0],c+dir[1])
        if (nr,nc) not in map and input[nr][nc] != '#':
            queue.append((time,nr,nc))
