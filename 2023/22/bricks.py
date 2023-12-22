from collections import defaultdict, deque
input = [l[:-1] for l in open('input.txt','r').readlines()]

bricks = []
dependencies = defaultdict(set)
class Brick:
    def __init__(self, line, idx):
        self.blocks = []
        self.idx = idx
        first, last_ = line.split('~')
        fx,fy,fz = list(map(int,first.split(',')))
        lx,ly,lz = list(map(int,last_.split(',')))

        vector = (lx-fx,ly-fy,lz-fz)
        mag = abs(max(vector))
        dir = list(map(lambda x: x//mag, vector)) if mag else [0,0,0]

        x,y,z = fx,fy,fz
        for _ in range(mag+1):
            self.blocks.append([x,y,z])
            x,y,z = x+dir[0], y+dir[1], z+dir[2]

        self.build_set()

    def build_set(self):
        self.block_set = set()
        for [x,y,z] in self.blocks:
            self.block_set.add((x,y,z))

    def lowest_z(self):
        return min(block[2] for block in self.blocks)
    
    def can_fall(self):
        for [x,y,z] in self.blocks:
            if z==1: return False
            for brick in bricks:
                if brick==self: continue
                if (x,y,z-1) in brick.block_set:
                    return False
        return True

    def fall(self):
        fell = self.can_fall()
        while self.can_fall():
            for block in self.blocks:
                block[2] -= 1

        if fell:
            self.build_set()
            dependencies[self] = set()
            self.set_dependencies()
            # print(self.idx, 'falls')
        return fell
    
    def supports(self,other_brick):
        if self==other_brick:
            return False
        if other_brick.lowest_z()==1:
            return False
        for [x,y,z] in self.blocks:
            if (x,y,z+1) in other_brick.block_set:
                return True
        return False
    
    def set_dependencies(self):
        for brick in bricks:
            if brick.supports(self):
                dependencies[brick].add(self) 
                

for i,line in enumerate(input):
    bricks.append(Brick(line, i))
bricks.sort(key=lambda b: b.lowest_z())
    
for brick in bricks:
    brick.set_dependencies()

queue = deque(bricks)
while queue:
    brick = queue.popleft()
    if brick.can_fall():
        for dep in dependencies[brick]:
            queue.append(dep)
        brick.fall()

# for brick in dependencies:
#     print(brick.idx, [b.idx for b in dependencies[brick]])

supporters = defaultdict(list)
for brick in bricks:
    for dep in dependencies[brick]:
        supporters[dep].append(brick)

# for brick in supporters:
#     print(brick.idx, [b.idx for b in supporters[brick]])

# part 1
safe = set()
for brick in bricks:
    can = True
    for dep in dependencies[brick]:
        if len(supporters[dep])==1:
            can=False
    if can:
        safe.add(brick)

# print(len(safe))
# print(safe)

# part 2
memo = dict()
def cascade(brick):
    if brick in memo:
        return memo[brick]
    if brick in safe:
        memo[brick] = 0
        return 0

    fallen=set()
    fallen.add(brick)
    q = deque(dependencies[brick])
    
    while q:
        curr = q.popleft()
        for dep in dependencies[curr]:
            q.append(dep)
        if all(sup in fallen for sup in supporters[curr]):
            fallen.add(curr)
    
    memo[brick] = len(fallen)-1
    return len(fallen)-1

for brick in bricks:
    cascade(brick)
print(sum(memo.values()))