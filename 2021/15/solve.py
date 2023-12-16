import heapq
input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [[int(n) for n in line] for line in input]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
R,C = len(grid),len(grid[0])

# part 2
def wrap(n):
    if n>9:
        return n-9
    else:
        return n
    
grid = [[wrap(grid[r%R][c%C] + (r//R) + (c//C)) for c in range(5*C)] for r in range(5*R)]

risks = [[10**20 for _ in range(5*C)] for _ in range(5*R)]
pq = [(0,0,0)]
visited = set([(0,0)])

while pq:
    (risk,r,c) = heapq.heappop(pq)

    if risk>=risks[r][c]:
        continue

    risks[r][c] = risk
    visited.add((r,c))

    for dir in dirs:
        nr,nc = r+dir[0],c+dir[1]
        if nr<0 or nc<0 or nr==5*R or nc==5*C:
            continue
        if (nr,nc) in visited:
            continue
        heapq.heappush(pq,(risk+grid[nr][nc],nr,nc))

print(risks[-1][-1])

# import heapq

# dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# R, C = len(grid), len(grid[0])
# print(R,C)

# # Initialize distances with infinity
# distances = [[float('inf') for _ in range(C)] for _ in range(R)]
# distances[0][0] = 0

# # Use a priority queue
# pq = [(0, 0, 0)]  # (distance, row, col)

# while pq:
#     dist, r, c = heapq.heappop(pq)

#     for dr, dc in dirs:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < R and 0 <= nc < C:
#             print(nr,nc, C)
#             new_dist = dist + grid[nr][nc]
#             if new_dist < distances[nr][nc]:
#                 distances[nr][nc] = new_dist
#                 heapq.heappush(pq, (new_dist, nr, nc))

# print(distances[-1][-1])