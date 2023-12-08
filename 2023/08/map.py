input = [l[:-1] for l in open('input.txt','r').readlines()]
steps = input[0]*100 # hehehe

nodes = {}

for line in input[2:]:
    line = line[:-1]
    node, children = line.split(' = (')
    l,r = children.split(', ')
    nodes[node] = {'L': l, 'R': r}

# part 1
i = 0
curr = 'AAA'
while curr != 'ZZZ':
    curr = nodes[curr][steps[i]]
    i+=1
print(i)

# part 2
i = 0
curr = [n for n in nodes if n[-1]=='A']

# def done():
#     for node in curr:
#         if node[-1] != 'Z':
#             return False
#     return True
finishes = []

# while not done(): # very long time
while len(finishes)<len(curr):
    for j in range(len(curr)):
        curr[j] = nodes[curr[j]][steps[i]]
        if curr[j][-1] == 'Z':
            # print(f'Node Index {j} reached Z after {i+1} steps')
            finishes.append(i+1)
    i+=1
print(i)
print(finishes)
from math import lcm
print(lcm(*finishes))