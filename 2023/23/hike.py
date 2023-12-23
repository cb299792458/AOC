input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(line) for line in input]
R,C = len(grid), len(grid[0])

longest = 0
import sys
sys.setrecursionlimit(2000)

def backtrack(r,c,path):
    if (r,c) in path:
        return
    path = path.copy()
    path.add((r,c))

    if r<0: return
    if r==R-1 and c==C-2:
        global longest
        longest=max(longest,len(path))
        return
    
    curr = grid[r][c]
    if curr=='#':
        return

    # part 1
    if curr in ['.','>']:
        backtrack(r,c+1,path)
    if curr in ['.','<']:
        backtrack(r,c-1,path)
    if curr in ['.','^']:
        backtrack(r-1,c,path)
    if curr in ['.', 'v']:
        backtrack(r+1,c,path)

    # # part 2
    # backtrack(r,c+1,path)
    # backtrack(r,c-1,path)
    # backtrack(r-1,c,path)
    # backtrack(r+1,c,path)

backtrack(0,1,set())

print(longest-1)