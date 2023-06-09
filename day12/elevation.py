from collections import deque
input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
# print(input)
grid = [[*line] for line in input]
# print(grid)

letters = 'abcdefghijklmnopqrstuvwxyz'
heights = dict()
for i in range(26):
    heights[letters[i]] = i
heights['S']=0
heights['E']=25
# print(heights)
dirs=[[1,0],[-1,0],[0,1],[0,-1]]

start=(None,None)
end=(None,None)

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c]=='S': start=(r,c)
        if grid[r][c]=='E': end=(r,c)

memo = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
seen = set()

# # part 1
# queue = deque([start])
# dist = 0
# while queue:
#     new_queue = deque()
#     for (r,c) in queue:
#         if (r,c) in seen: continue
#         seen.add((r,c))

#         if (r,c)==end:
#             print(dist)
#             break
            
#         for d in dirs:
#             nr,nc=r+d[0],c+d[1]
#             if nr<0 or nc<0 or nr==len(grid) or nc==len(grid[0]): continue
#             if heights[grid[nr][nc]] <= heights[grid[r][c]] + 1:
#                 new_queue.append((nr,nc))
#     dist+=1
#     queue=new_queue

# part 2
queue = deque([end])
dist = 0
while queue:
    new_queue = deque()
    for (r,c) in queue:
        if (r,c) in seen: continue
        seen.add((r,c))

        if heights[grid[r][c]]==0:
            print(dist)
            break
            
        for d in dirs:
            nr,nc=r+d[0],c+d[1]
            if nr<0 or nc<0 or nr==len(grid) or nc==len(grid[0]): continue
            if heights[grid[nr][nc]] >= heights[grid[r][c]] - 1:
                new_queue.append((nr,nc))
    dist+=1
    queue=new_queue

