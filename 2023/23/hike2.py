from collections import deque
input = [l[:-1] for l in open('input.txt','r').readlines()]
grid = [list(line) for line in input]
R,C = len(grid), len(grid[0])
dirs = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

def count_connections(point):
    r,c = point.location
    count = 0
    for d in dirs:
        nr,nc=r+d[0],c+d[1]
        if nr>-1 and nr<R and grid[nr][nc]!='#':
            count += 1
    return count

points = dict()
class Point:
    def __init__(self,r,c) -> None:
        self.location = (r,c)
        self.connects = []
        for d in dirs:
            nr,nc=r+d[0],c+d[1]
            if nr>-1 and nr<R and grid[nr][nc]!='#':
                self.connects.append((nr,nc))

for r in range(1,R-1):
    for c in range(1,C-1):
        if grid[r][c]!='#':
            point = Point(r,c)
            points[point.location] = point
points[(0,1)] = Point(0,1)
points[(R-1,C-2)] = Point(R-1,C-2)

nodes = dict()
class Node:
    def __init__(self, points, connects) -> None:
        self.points = points
        self.connects = connects
processed = set()

for point in points.values():
    if point in processed: continue
    if count_connections(point)!=2 or point.location==(0,1) or point.location==(R-1,C-2):
        processed.add(point)

        node = Node([point.location], point.connects)
        nodes[node.points[0]] = node
    else:
        hallway = deque([point])

        while True:
            n1 = points[hallway[-1].connects[0]]
            n2 = points[hallway[-1].connects[1]]
            if n1 not in hallway and count_connections(n1)==2 and n1 not in processed:
                hallway.append(n1)
            elif n2 not in hallway and count_connections(n2)==2 and n2 not in processed:
                hallway.append(n2)
            else:
                break

        while True:
            n1 = points[hallway[0].connects[0]]
            n2 = points[hallway[0].connects[1]]
            if n1 not in hallway and count_connections(n1)==2 and n1 not in processed:
                hallway.appendleft(n1)
            elif n2 not in hallway and count_connections(n2)==2 and n2 not in processed:
                hallway.appendleft(n2)
            else:
                break
        
        for point in hallway:
            processed.add(point)

        new_points = [p.location for p in hallway]
        connects = hallway[0].connects + hallway[-1].connects
        connects = [c for c in connects if c not in new_points]
        # print(new_points,connects)
        node = Node(new_points, connects)

        nodes[node.points[0]] = node
        nodes[node.points[-1]] = node
        # print(node.points)
# print(nodes[(1,1)].connects)

longest = 0
def backtrack(node,dist,path):
    if node in path:
        return
    path.add(node)
    dist += len(node.points)

    if node.points[0]==(R-1,C-2):
        global longest
        longest = max(longest,dist)
        return

    path = path.copy()

    for tup in node.connects:
        backtrack(nodes[tup], dist, path)

backtrack(nodes[(0,1)],0,set())
print(longest-1)