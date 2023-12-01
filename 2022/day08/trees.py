input=open('input.txt','r').readlines()
input=[a[:-1] for a in input]

trees = [[int(num) for num in line] for line in input]
# print(trees)
visible = [[False for _ in row] for row in trees]
# print(visible)
ROWS = len(trees)
COLS = len(trees[0])

for row in range(ROWS):
    pmax = -1
    for col in range(COLS):
        if trees[row][col]>pmax:
            visible[row][col] = True
            pmax = trees[row][col]

for row in range(ROWS):
    pmax = -1
    for col in range(COLS-1,-1,-1):
        if trees[row][col]>pmax:
            visible[row][col] = True
            pmax = trees[row][col]

for col in range(COLS):
    pmax = -1
    for row in range(ROWS):
        if trees[row][col]>pmax:
            visible[row][col] = True
            pmax = trees[row][col]
for col in range(COLS):
    pmax = -1
    for row in range(ROWS-1,-1,-1):
        if trees[row][col]>pmax:
            visible[row][col] = True
            pmax = trees[row][col]

count=0
for row in range(ROWS):
    for col in range(COLS):
        if visible[row][col]: count+=1

print(count)

max_score = 0
dirs=[
    [0,1],
    [0,-1],
    [1,0],
    [-1,0],
]
for row in range(ROWS):
    for col in range(COLS):
        score=1
        for dir in dirs:
            nr,nc=row+dir[0],col+dir[1]
            steps=0
            height=trees[row][col]

            while -1<nr<ROWS and -1<nc<COLS and trees[nr][nc]<height:
                nr,nc=nr+dir[0],nc+dir[1]
                steps+=1
            if -1<nr<ROWS and -1<nc<COLS: steps+=1
            if (row,col)==(14,49): print(steps)
            score*=(steps)
        
        max_score=max(max_score,score)
        if score==201684: print(row,col)
print(max_score)

# scores = [[1 for _ in row] for row in trees]
# for row in range(ROWS):
#     pmax = 10
#     streak=0
#     for col in range(COLS):
#         if trees[row][col]>pmax:
#             pmax = trees[row][col]
#         else:
#             streak=1
#         scores[row][col]*=streak


# for row in range(ROWS):
#     pmax = -1
#     for col in range(COLS-1,-1,-1):
#         if trees[row][col]>pmax:
#             visible[row][col] = True
#             pmax = trees[row][col]

# for col in range(COLS):
#     pmax = -1
#     for row in range(ROWS):
#         if trees[row][col]>pmax:
#             visible[row][col] = True
#             pmax = trees[row][col]
# for col in range(COLS):
#     pmax = -1
#     for row in range(ROWS-1,-1,-1):
#         if trees[row][col]>pmax:
#             visible[row][col] = True
#             pmax = trees[row][col]
