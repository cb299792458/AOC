input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
input = [(a[0], int(a.split()[1])) for a in input]
dirs = { 'U': [-1,0], 'D': [1,0], 'R': [0,1], 'L': [0,-1] }

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self,dir):
        self.x = self.x + dirs[dir][1]
        self.y = self.y + dirs[dir][0]
    def follow(self,prev):
        myx=self.x
        myy=self.y

        if abs(prev.x-self.x)>1 and abs(prev.y-self.y)>1:
            self.x=int((prev.x+self.x)/2)
            self.y=int((prev.y+self.y)/2)

        elif abs(prev.x-self.x)>1:
            self.y=prev.y
            self.x=int((prev.x+self.x)/2)
        elif abs(prev.y-self.y)>1:
            self.x=prev.x
            self.y=int((prev.y+self.y)/2)


# h = Knot()
# t = Knot()
seen = set([(0,0)])

# # part 1
# for move in input:
#     [dir,num] = move

#     for _ in range(num):
#         h.move(dir)
#         t.follow(h)
        
#         seen.add((t.x,t.y))
# print(len(seen))


rope = [None]*10
for i in range(10):
    rope[i]=Knot()
for move in input:
    [dir,num] = move
    # print((dir,num))
    for _ in range(num):
        rope[0].move(dir)
        for j in range(1,10):
            if rope[j].follow(rope[j-1])=='err':
                for k in rope:
                    print(k.x,k.y)
                
            if(j==9):

                if (rope[-1].x,rope[-1].y) not in seen:
                    # print((rope[-1].x,rope[-1].y))
                    seen.add((rope[-1].x,rope[-1].y))
print(len(seen))

