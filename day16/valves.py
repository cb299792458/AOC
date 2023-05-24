input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
from collections import deque
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
        # self.dists.sort(key=lambda x: valves[x[0]].flow / x[1], reverse=True)

        self.dist_dict = dict()
        for a in self.dists:
            self.dist_dict[a[0]] = a[1]

# parse input
for line in input:
    words = line.split()
    name=words[1]
    flow=int(words[4][5:-1])
    neighbors = words[9:]
    neighbors = [n.strip(',') for n in neighbors]
    valves[name] = Valve(name,flow,neighbors)

# make adjacency list
to_open = set()
for v in valves.values():
    v.make_adj_list()
    if v.flow: to_open.add(v)

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

# make dict of distance to each other relevant value
for node in to_open:
    node.make_dist_list()
valves['AA'].make_dist_list()

class Search:
    def __init__(self,node,opened,time_left,pressure) -> None:
        self.node = node
        self.opened = opened
        self.time_left = time_left
        self.pressure = pressure

# bfs w/ each possible step as instance of "search" class
start = Search(valves['AA'],set(),30,0)
best = {30:0} # key is time_left, value is pressure
queue = deque([start])

while queue:
    curr = queue.popleft()

    # end case
    if curr.time_left<0: 
        continue

    # too slow
    too_slow = False
    for time_left in best.keys():
        if curr.time_left <= time_left and best[time_left] > curr.pressure: too_slow = True
    if too_slow: continue

    # save best pressure
    if curr.time_left not in best or best[curr.time_left] < curr.pressure:
        # print('hit')
        best[curr.time_left] = curr.pressure

    # explore new nodes
    for next_node in to_open:
        seen = curr.opened.copy()
        if next_node in seen: continue
        seen.add(next_node)

        time_left = curr.time_left
        time_left -= curr.node.dist_dict[next_node.name] # travel time
        time_left -= 1 # time to open valve
        queue.append(Search(next_node, seen, time_left, curr.pressure+(time_left*next_node.flow)))

    # if curr.time_left==1: print(len(seen))

# the value with the lowest key should be the best pressure, but it changes?!
print(best)
print(max(best.values()))