from collections import defaultdict

input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
input = [[c for c in line] for line in input]

elf_pos = set()
for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c]=='#': elf_pos.add((r,c))
# print(elves)

N,S,W,E = 'N','S','W','E'
dir_order = [N,S,W,E]
dirs = {
    N: ( (-1,0), (-1,-1), (-1,+1), ),
    S: ( (+1,0), (+1,-1), (+1,+1), ),
    W: ( (0,-1), (-1,-1), (+1,-1), ),
    E: ( (0,+1), (-1,+1), (+1,+1), ),
}

class Elf:
    def __init__(self,r,c) -> None:
        self.r = r
        self.c = c

    def move(self,r,c):
        self.r = r
        self.c = c

    def propose(self):
        adj = (
            (-1,-1),
            (-1,0),
            (-1,+1),
            (0,-1),
            (0,+1),
            (+1,-1),
            (+1,0),
            (+1,+1),
        )
        alone=True
        for a in adj:
            (nr,nc) = (self.r+a[0],self.c+a[1])
            if (nr,nc) in elf_pos: alone=False
        if alone: return None


        for dir in dir_order:
            tups = dirs[dir]
            if (self.r+tups[0][0],self.c+tups[0][1]) not in elf_pos and (self.r+tups[1][0],self.c+tups[1][1]) not in elf_pos and (self.r+tups[2][0],self.c+tups[2][1]) not in elf_pos:
                return (self.r+tups[0][0],self.c+tups[0][1])
        return None
    
all_elves = []
for (r,c) in elf_pos:
    all_elves.append(Elf(r,c))



for _ in range(10):
    proposals = defaultdict(list)

    # list of all elves proposing a tuple position
    for elf in all_elves:
        proposal = elf.propose()
        if proposal: proposals[proposal].append(elf)

    # move all elves if they are the only elf proposing to move there
    for tup in proposals.keys():
        if len(proposals[tup])==1:
            elf = proposals[tup][0]

            elf_pos.remove((elf.r,elf.c))
            elf.move(tup[0],tup[1])
            elf_pos.add(tup)

    dir_order = dir_order[1:] + [dir_order[0]]



# print(elf_pos)
minr=minc=float('inf')
maxr=maxc=float('-inf')
for pos in elf_pos:
    minr = min(minr,pos[0])
    maxr = max(maxr,pos[0])
    minc = min(minc,pos[1])
    maxc = max(maxc,pos[1])

print((maxr-minr+1)*(maxc-minc+1)-len(elf_pos))










# print(input)
# for line in input:
#     print(''.join(line))

# for r in range(-15,15):
#     print(''.join(['#' if (r,c) in elf_pos else '.' for c in range(-15,15)]))
