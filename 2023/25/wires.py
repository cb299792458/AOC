from collections import defaultdict, deque
input = [l[:-1] for l in open('input.txt','r').readlines()]

adjs = defaultdict(list)
for line in input:
    first, rests = line.split(': ')
    for rest in rests.split(' '):
        adjs[first].append(rest)
        adjs[rest].append(first)
total = len(adjs)
nodes = list(adjs.keys())

edges = []
for line in input:
    first, rests = line.split(': ')
    for rest in rests.split(' '):
        edges.append((first,rest))
E=len(edges)

uses = defaultdict(int)
def djikstra(orig, dest):
    q = deque([[orig]])
    seen = set()

    while q:
        path = q.popleft()
        if path[-1]==dest:
            for i in range(len(path)-1):
                edge = [path[i],path[i+1]]
                edge.sort()
                edge = tuple(edge)
                uses[edge] += 1
            return
        node = path[-1]
        for adj in adjs[node]:
            if adj in seen:
                continue
            seen.add(adj)
            q.append(path+[adj])

for i in range(0,len(nodes),10):
    for j in range(i+1,len(nodes),10):
        djikstra(nodes[i],nodes[j])

uses = list(uses.items())
uses.sort(key=lambda p: p[1])
print(uses[-3:])
broken = [u[0] for u in uses[-3:]]

def get_size(node, broken):
    seen = set()
    dfs(node, broken, seen)
    return len(seen)

def dfs(node, broken, seen):
    if node in seen: return
    seen.add(node)

    for adj in adjs[node]:
        if (adj,node) in broken or (node,adj) in broken:
            continue
        dfs(adj, broken, seen)

size = get_size(input[0].split(':')[0], broken)
print(size, total-size, (total-size)*size)