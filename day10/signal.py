input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
# print(input)
from collections import deque

times = deque([20,60,100,140,180,220])

x=1
cycle=0
sum=0
output = ['.']*240

# # part 1
# for line in input:
#     cycle+=1

#     if times and cycle>=times[0]:
#         sum+=x*times.popleft()

#     if line[:4]=='addx':
#         cycle+=1

#         if times and cycle>=times[0]:
#             sum+=x*times.popleft()
#         x+=int(line[5:])

# part 2
def draw():
    if abs(x-cycle%40)<2:
        output[cycle]='#'

for line in input:
    draw()
    cycle+=1
    if line[:4]=='addx':
        draw()
        cycle+=1
        x+=int(line[5:])
    print(x)

    
for start in range(0,240,40):
    print(''.join(output[start:start+40]))