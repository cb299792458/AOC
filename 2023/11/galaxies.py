input = [l[:-1] for l in open('input.txt','r').readlines()]
input = [list(string) for string in input]

# # part 1
# expanded = []
# for row in input:
#     if all(c=='.' for c in row):
#         expanded.append(row)
#     expanded.append(row) 
# expanded = list(zip(*expanded))
# input = []
# for row in expanded:
#     if all(c=='.' for c in row):
#         input.append(row)
#     input.append(row)
# input = list(zip(*input))

# tups = []
# R,C = len(input), len(input[0])
# for r in range(R):
#     for c in range(C):
#         if input[r][c]=='#':
#             tups.append((r,c))

# def dist(t1,t2):
#     return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

# lengths = 0
# for i in range(len(tups)):
#     for j in range(i,len(tups)):
#         lengths += dist(tups[i],tups[j])
# print(lengths)

# part 2
empty_rows = []
empty_cols = []
for r,row in enumerate(input):
    if all(c=='.' for c in row):
        empty_rows.append(r)
for c in range(len(input[0])):
    if all(input[r][c]=='.' for r in range(len(input))):
        empty_cols.append(c)

def dist(t1,t2):
    r1,c1 = t1
    r2,c2 = t2
    expansions = 0
    for row in empty_rows:
        if r1<row<r2 or r2<row<r1:
            expansions += 1
    for col in empty_cols:
        if c1<col<c2 or c2<col<c1:
            expansions += 1
    return abs(r1-r2) + abs(c1-c2) + (999999*expansions)

tups = []
R,C = len(input), len(input[0])
for r in range(R):
    for c in range(C):
        if input[r][c]=='#':
            tups.append((r,c))

lengths = 0
for i in range(len(tups)):
    for j in range(i,len(tups)):
        lengths += dist(tups[i],tups[j])
print(lengths)