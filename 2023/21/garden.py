input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[c for c in line] for line in input]
R,C = len(grid), len(grid[0])
dirs = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

# # part 1
# S = (None,None)
# for r in range(R):
#     for c in range(C):
#         if grid[r][c]=='S':
#             S = (r,c)
# # print(S)

# odds_ = set([])
# evens = set([S])

# steps = 64
# for i in range(steps):
#     starts = odds_ if i%2 else evens
#     finals = evens if i%2 else odds_

#     for (r,c) in starts:
#         for d in dirs:
#             nr, nc = r+d[0], c+d[1]
#             if -1<nr<R and -1<nc<C and grid[nr][nc]!='#':
#                 finals.add((nr,nc))

# print(len(finals))
grid = grid * 9
grid = [line*9 for line in grid]

mid = 9*R//2
S = (mid,mid)

def solve(steps):
    odds_ = set([])
    evens = set([S])

    for i in range(steps):
        starts = odds_ if i%2 else evens
        finals = evens if i%2 else odds_

        for (r,c) in starts:
            for d in dirs:
                nr, nc = r+d[0], c+d[1]
                if -1<nr<9*R and -1<nc<9*C and grid[nr][nc]!='#':
                    finals.add((nr,nc))
    return len(finals)

# for k in range(3):
#     print(k, solve(131*k+65))

f0 = 3911
f1 = 34786
f2 = 96435

"""
f0 = c
f1 = a + b + c
f2 = 4a + 2b + c
2a = f2 - 2f1 + c
"""

c = f0
a = (f2 - 2*f1 + c)//2
b = f1-a-c
print(a,b,c)

def f(x):
    return (a*x*x) + (b*x) + c

for i in range(10):
    print(f(i))
print(f(26501365//131))