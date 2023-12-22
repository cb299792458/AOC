input = [l[:-1] for l in open('input.txt','r').readlines()]

bricks = []
class Brick:
    def __init__(self, line):
        self.blocks = []
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
        # self.fall()

    def lowest_z(self):
        return min(block[2] for block in self.blocks)
    
    def can_fall(self):
        for (x,y,z) in self.blocks:
            if z==0: return False
            for brick in bricks:
                if brick==self: continue
                for (nx,ny,nz) in brick.blocks:
                    if nx==x and ny==y and nz==z-1:
                        return False
        return True

    def fall(self):
        fell = self.can_fall()
        while self.can_fall():
            for block in self.blocks:
                block[2] -= 1
        return fell
    
    def supports(self,other_brick):
        for (x,y,z) in self.blocks:
            for (ox,oy,oz) in other_brick.blocks:
                if x==ox and y==oy and z==oz-1:
                    return True
        return False
        
for line in input:
    bricks.append(Brick(line))
# bricks.sort(key=lambda b: b.lowest_y())

fallen = True
while fallen:
    fallen = False
    for brick in bricks:
        if brick.fall():
            fallen = True

disintegrate = 0
for brick in bricks:
    temp = brick.blocks

    can_disintegrate = True
    for other_brick in bricks:
        if brick==other_brick: continue
        if brick.supports(other_brick):

            brick.blocks = []
            if other_brick.can_fall():
                can_disintegrate = False
            brick.blocks = temp
    
    if can_disintegrate:
        disintegrate += 1

print(disintegrate)
