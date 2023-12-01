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

# print(len(to_open))
# print(valves['AA'].dist_dict)
# print(valves['DD'].flow)
# for valve in to_open:
#     print(valve.name)

time = 26
# human_open = to_open.copy()

pairs = []
q = deque()
q.append((list(to_open), [], []))
while q:
    (to_open_list,human,elephant) = q.popleft()

    if not to_open_list:
        if len(human)>6 and len(elephant)>6: pairs.append([human,elephant])
        continue

    to_open_list_copy = to_open_list.copy()
    curr = to_open_list_copy.pop()
    q.append((to_open_list_copy,human+[curr],elephant))
    q.append((to_open_list_copy,human,elephant+[curr]))

# print(len(to_open))
# print(len(pairs))
# print(pairs[0])

best = 0
for human, elephant in pairs:
    human=set(human)
    elephant=set(elephant)


    queue = deque()
    queue.append((valves['AA'], human, 0, time))
    human_best = 0

    while queue:
        (current, still_to_open, pressure, time_left) = queue.popleft()
        if time_left<0: continue
        human_best = max(human_best,pressure)

        for node in still_to_open:
            set_copy = still_to_open.copy()
            set_copy.remove(node)

            new_time = time_left
            new_time -= current.dist_dict[node.name] # travel time
            new_time -= 1 # time to open valve

            queue.append((node, set_copy, pressure + (node.flow*new_time), new_time))
    
    
    
    queue = deque()
    queue.append((valves['AA'], elephant, 0, time))
    elephant_best = 0

    while queue:
        (current, still_to_open, pressure, time_left) = queue.popleft()
        if time_left<0: continue
        elephant_best = max(elephant_best,pressure)

        for node in still_to_open:
            set_copy = still_to_open.copy()
            set_copy.remove(node)

            new_time = time_left
            new_time -= current.dist_dict[node.name] # travel time
            new_time -= 1 # time to open valve

            queue.append((node, set_copy, pressure + (node.flow*new_time), new_time))

    best = max(best, human_best+elephant_best)

print(best)