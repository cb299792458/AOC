from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]
adjs = defaultdict(list)

for line in input:
    [orig,dest] = line.split('-')
    adjs[orig].append(dest)
    adjs[dest].append(orig)

paths = 0
def dfs(node, seen=set()):
    if node == 'end':
        global paths
        paths +=1
        return
    if node in seen:
        return
    if node.islower():
        seen.add(node)

    for adj in adjs[node]:
        dfs(adj,seen.copy())

dfs('start')
print(paths)

paths = 0
def dfs2(node, visits=defaultdict(int)):
    # print(sorted(visits.values()))
    if len(visits.values())>1 and (sorted(visits.values())[-2]>1 or sorted(visits.values())[-1]>2):
        return
    if node == 'end':
        global paths
        paths +=1
        return
    if node.islower():
        visits[node]+=1

    for adj in adjs[node]:
        if adj == 'start':
            continue
        dfs2(adj,visits.copy())

dfs2('start')
print(paths)
