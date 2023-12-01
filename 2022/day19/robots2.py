from collections import defaultdict, deque
import copy
input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

# useful constants
ORE='ore'
CLAY='clay'
GEO='geode'
OBS='obsidian'
materials = [ORE,CLAY,GEO,OBS]

# parse input data
blueprints = dict()
for line in input:
    words = line.split()
    
    id = int(words[1][:-1])
    robot_costs = dict()

    robot_costs[ORE] = {ORE: int(words[6])}
    robot_costs[CLAY] = {ORE: int(words[12])}
    robot_costs[OBS] = {ORE: int(words[18]), CLAY: int(words[21])}
    robot_costs[GEO] = {ORE: int(words[27]), OBS: int(words[30])}

    blueprints[id] = robot_costs
# print(blueprints)

class Inventory:
    def __init__(self, bp, bots=defaultdict(int), mats=defaultdict(int), time=32) -> None:
        self.bp = bp
        self.bots = bots
        self.mats = mats
        self.time = time

    def harvest(self):
        for mat in materials:
            self.mats[mat] += self.bots[mat]
        self.time -= 1
        return self

    def can_build(self,mat):
        if mat==ORE or mat==CLAY: return True
        if mat==OBS: return not not self.bots[CLAY]
        if mat==GEO: return not not self.bots[OBS]

    def should_build(self,mat):
        if mat==GEO: return True
        if mat==OBS: return self.bots[OBS]<blueprints[self.bp][GEO][OBS]
        if mat==CLAY: return self.bots[CLAY]<blueprints[self.bp][OBS][CLAY]
        if mat==ORE:
            req=0
            for recipe in blueprints[self.bp].values():
                req=max(req,recipe[ORE])
            return self.bots[ORE]<req
    
    def has_mats(self,bot):
        for mat in blueprints[self.bp][bot]:
            if self.mats[mat] < blueprints[self.bp][bot][mat]:
                return False
        return True

    def build(self,bot):
        while not self.has_mats(bot):
            self.harvest()
        
        costs = blueprints[self.bp][bot]
        for mat in costs:
            self.mats[mat] -= costs[mat]

        self.harvest()
        self.bots[bot]+=1

    # find max possible geodes from this state
    def possible_geodes(self):
        return self.mats[GEO] + (self.bots[GEO]*self.time) + int((self.time*(self.time-1))/2)
    

    

quality_levels = defaultdict(int)
max_geos = defaultdict(int)
for bp in blueprints:
    max_geodes=0
    start = Inventory(bp)
    start.bots[ORE] = 1

    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current.time<=0: continue
        max_geodes=max(max_geodes,current.mats[GEO]+current.bots[GEO]*current.time)

        # can't catch best
        if current.possible_geodes() < max_geodes: continue
    
        # do nothing
        # new = Inventory(current.bp,current.bots.copy(),current.mats.copy(),current.time)
        # queue.append(new.harvest())
        
        # try to build each bot
        for bot in materials:
            if current.can_build(bot) and current.should_build(bot):
                new = Inventory(current.bp,current.bots.copy(),current.mats.copy(),current.time)
                new.build(bot)
                queue.append(new)
        
        # new = Inventory(current.bp,current.bots.copy(),current.mats.copy(),current.time)
        # queue.append(new)

    quality_levels[bp] = bp * max_geodes
    max_geos[bp] = max_geodes

print(quality_levels)
print(sum(quality_levels.values()))


from math import prod
print(prod(max_geos.values()))