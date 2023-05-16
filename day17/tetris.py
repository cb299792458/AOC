input = open('input.txt','r').readlines()[0][:-1]
# print(input)

chamber = [[c for c in '012345678']]+[['|']+['.']*7+['|'] for _ in range(4)]

start_height=4
rock_idx=0
rock_pos = (start_height,3)

BLOCKS = [
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,1],[1,0],[1,1],[1,2],[2,1]],
    [[0,0],[0,1],[0,2],[1,2],[2,2]],
    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[1,0],[1,1]],
]

def rock_push(dir):
    global rock_pos
    (r,c)=rock_pos
    delta = -1 if dir=='<' else 1
    
    for block in BLOCKS[rock_idx%5]:
        new_pos = (r+block[0],c+block[1])
        if chamber[new_pos[0]][new_pos[1]+delta]!='.': return

    rock_pos=(r,c+delta)

def rock_drop():
    global rock_pos
    (r,c)=rock_pos

    for block in BLOCKS[rock_idx%5]:
        new_pos = (r+block[0],c+block[1])
        if chamber[new_pos[0]-1][new_pos[1]]!='.': return False

    rock_pos=(r-1,c)
    return True

def place_rocks():
    global rock_pos
    (r,c)=rock_pos
        
    for block in BLOCKS[rock_idx%5]:
        new_pos = (r+block[0],c+block[1])
        chamber[new_pos[0]][new_pos[1]] = '#'
    
def print_chamber():
    for line in chamber[::-1]:
        print(''.join(line))

def find_start_height():
    global rock_pos
    global start_height
    rock_heights=[0,2,2,3,1]

    start_height=max( start_height , rock_pos[0] + rock_heights[rock_idx%5] + 4)
    if rock_idx==2021: print(start_height)

for dir in input:
    rock_push(dir)
    if not rock_drop():
        find_start_height()
        place_rocks()
        rock_idx+=1

        while start_height>len(chamber)-1-3:
            chamber.append(['|']+['.']*7+['|'])
        rock_pos=(start_height,3)
    

while chamber[-1]==['|']+['.']*7+['|']: chamber.pop()
print_chamber()

    




