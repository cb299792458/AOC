input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

valves=dict()

class Valve:
    def __init__(self,name,flow,neighbors):
        self.name=name
        self.flow=flow
        self.neighbors=neighbors
        self.adj=[]
        self.dists=[]

    def make_adj_list(self):
        for n in self.neighbors:
            self.adj.append(valves[n])

    def make_dist_list(self):
        for a in to_open:
            if a==self: continue
            self.dists.append((a.name,dijkstra_distance(self,a)))
        self.dists.sort(key=lambda x: valves[x[0]].flow / x[1], reverse=True)


for line in input:
    words = line.split()
    name=words[1]
    flow=int(words[4][5:-1])
    neighbors = words[9:]
    neighbors = [n.strip(',') for n in neighbors]
    valves[name] = Valve(name,flow,neighbors)

to_open = set()
for v in valves.values():
    v.make_adj_list()
    if v.flow: to_open.add(v)

"""
Strategy:
find only valves with flow rate > 0
start at curr = AA
find largest flow rate / distance away
    what if there's a cluster that's far away?
    
memo[minute] = max release at that minute
    different paths
"""

def dijkstra_distance(start,end):
    dist=0
    queue=[start]
    while queue:
        new_queue=[]
        for node in queue:
            if node==end: return dist
            new_queue += node.adj
        queue=new_queue
        dist+=1

for node in to_open:
    node.make_dist_list()
valves['AA'].make_dist_list()

minute=0
curr = valves['AA']
seen=set()
pressure = 0

while minute <= 4:
    seen.add(curr)

    for node in curr.dists:
        if valves[node[0]] in seen: continue

        print(node[0])
        minute+=node[1]
        curr=valves[node[0]]
        minute+=1
        pressure += curr.flow*(4-minute)
        break
    if curr in seen: break

print(pressure)