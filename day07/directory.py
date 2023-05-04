input=open('input.txt','r').readlines()
input=[a[:-1] for a in input]

system = dict()
class Dir:
    def __init__(self,name,parent):
        # print(f'making a dir named {name} under {parent.name if parent else None}')
        self.name = parent.name + '/' + name if parent else '/'
        self.children = []
        self.files = []
        self.parent = parent
        system[self.name] = self

    def size(self):
        res=0

        for file in self.files:
            res += file[0]
        
        for child in self.children:
            res+=child.size()

        return res
    
    def __str__(self):
        return f'I am a directory named {self.name} of size {self.size()} with parent {self.parent.name if self.parent else None}'

root = Dir('/',None)
curr = root

for command in input[1:]:
    cmd = command.split()
    if cmd[0]=='$' and cmd[1]=='cd':
        target = cmd[2]
        if target=='..':
            curr = curr.parent
        else:
            curr = system[curr.name + '/' + target]
    elif cmd[0]=='$' and cmd[1]=='ls':
        pass

    # child directory
    elif cmd[0]=='dir':
        dir_name=cmd[1]
        curr.children.append(Dir(dir_name,curr))

    # file
    else:
        file_size=int(cmd[0])
        file_name=cmd[1]
        curr.files.append((file_size,file_name))


sum = 0

# get part 1 answer
for dir in system.values():
    if dir.size()<=100000:
        sum += dir.size()


# get part 2 answer
delete = float('inf')
for dir in system.values():
    if 70000000-system['/'].size()+dir.size()>=30000000:
        delete=min(delete,dir.size())
print(delete)