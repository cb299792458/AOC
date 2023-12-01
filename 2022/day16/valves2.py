input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
from collections import deque
from time import time
begin = time()
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
# print(valves['AA'].dist_dict)

class Search:
    def __init__(self,mtarget,mdelay,etarget,edelay,opened,time_left,pressure,actually_opened = set()) -> None:
        self.mtarget = mtarget
        self.mdelay = mdelay
        self.etarget = etarget
        self.edelay = edelay
        self.opened = opened
        self.time_left = time_left
        self.pressure = pressure
        self.actually_opened = actually_opened


# bfs w/ each possible step as instance of "search" class
total_time=26
start = Search(valves['AA'],0,valves['AA'],0,set(),total_time,0)
best = {total_time:[0,[]]} # key is time_left, value is pressure
queue = deque([start])

while queue:
    curr = queue.popleft()

    # end case
    if curr.time_left<0: 
        continue

    # too slow
    too_slow = False
    for time_left in best.keys():
        if curr.time_left <= time_left and best[time_left][0] > curr.pressure: too_slow = True
    if too_slow: continue

    # save best pressure
    if curr.time_left not in best or best[curr.time_left][0] < curr.pressure:
        best[curr.time_left] = [curr.pressure, [v.name for v in curr.opened]]


    # send ele to new node
    if not curr.edelay:
        curr.opened.add(curr.etarget)

        # curr.actually_opened.add(curr.etarget)
        for node in to_open:
            if node in curr.opened or node==curr.mtarget or node==curr.etarget: continue
            
            time_to_open = 1 + curr.etarget.dist_dict[node.name]
            if time_to_open >= curr.time_left: continue

            queue.append(
                Search(curr.mtarget,curr.mdelay,node,time_to_open,curr.opened.copy(),curr.time_left,
                       curr.pressure
                )
            )
        # continue

    # send me to new node
    if not curr.mdelay:
        # curr.actually_opened.add(curr.mtarget)
        curr.opened.add(curr.mtarget)

        for node in to_open:
            if node in curr.opened or node==curr.mtarget or node==curr.etarget: continue
            
            time_to_open = 1 + curr.mtarget.dist_dict[node.name]
            if time_to_open >= curr.time_left: continue


            queue.append(
                Search(node,time_to_open,curr.etarget,curr.edelay,curr.opened.copy(),curr.time_left,
                       curr.pressure
                )
            )
        # continue



    # neither redirected
    curr.time_left-=1
    curr.mdelay-=1
    curr.edelay-=1
    for valve in curr.opened:
        curr.pressure += valve.flow


    queue.append(curr)





# the value with the lowest key should be the best pressure, but it changes?!
print(best)
# print(max(best.values()))
print(f"{time() - begin} seconds")
