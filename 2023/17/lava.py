import heapq
from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]
input = [[int(n) for n in line] for line in input]

R,C = len(input), len(input[0])
N,S,E,W='N','S','E','W'
# dirs = [(1,0),(-1,0),(0,1),(0,-1)]

visited = set()
best = 10**20

# # part 1 (worked?!)
# pq = [(-2,0,0,None,None,None)]
# while pq:
#     (loss,r,c,prev1,prev2,prev3) = heapq.heappop(pq)

#     if r<0 or c<0 or r==R or c==C:
#         continue
#     loss += input[r][c]

#     if r==R-1 and c==C-1:
#         best = min(best,loss)
#         continue

#     if (r,c,prev1,prev2,prev3) in visited:
#         continue
#     visited.add((r,c,prev1,prev2,prev3))

#     if not prev1==W and not (prev1==prev2==prev3==E):
#         nr,nc = r,c+1
#         heapq.heappush(pq,(loss,nr,nc,E,prev1,prev2))
#     if not prev1==E and not (prev1==prev2==prev3==W):
#         nr,nc = r,c-1
#         heapq.heappush(pq,(loss,nr,nc,W,prev1,prev2))
#     if not prev1==N and not (prev1==prev2==prev3==S):
#         nr,nc = r+1,c
#         heapq.heappush(pq,(loss,nr,nc,S,prev1,prev2))
#     if not prev1==S and not (prev1==prev2==prev3==N):
#         nr,nc = r-1,c
#         heapq.heappush(pq,(loss,nr,nc,N,prev1,prev2))
# print(best)

# part 2
pq = [(-input[0][0],0,0,None,0)] # heat loss (skipping first), row, col, previous direction, same direction streak
memo = defaultdict(lambda: 10**20)

while pq:
    (loss,r,c,dir,num) = heapq.heappop(pq)

    if r<0 or c<0 or r==R or c==C:
        continue

    loss += input[r][c]
    if r==R-1 and c==C-1 and num>3:
        best = min(best,loss)
        continue

    # if (r,c,dir,num) in visited:
    #     continue
    # visited.add((r,c,dir,num))
    if memo[(r,c,dir,num)] < loss:
        continue
    memo[(r,c,dir,num)] = loss

    if dir==N and num<10:
        heapq.heappush(pq,(loss,r-1,c,N,num+1))
    if dir==S and num<10:
        heapq.heappush(pq,(loss,r+1,c,S,num+1))
    if dir==E and num<10:
        heapq.heappush(pq,(loss,r,c+1,E,num+1))
    if dir==W and num<10:
        heapq.heappush(pq,(loss,r,c-1,W,num+1))

    if not num or dir in [E,W] and num>3:
        heapq.heappush(pq,(loss,r-1,c,N,1))
        heapq.heappush(pq,(loss,r+1,c,S,1))
    if not num or dir in [N,S] and num>3:
        heapq.heappush(pq,(loss,r,c+1,E,1))
        heapq.heappush(pq,(loss,r,c-1,W,1))
print(best)

# for k,v in memo.items():
#     if k[0]==R-1 and k[1]==C-1:
#         print(v)