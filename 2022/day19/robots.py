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
    def __init__(self, bp, bots=defaultdict(int), mats=defaultdict(int), time=14) -> None:
        self.bp = bp
        self.bots = bots
        self.mats = mats
        self.time = time

    def harvest(self):
        for mat in materials:
            self.mats[mat] += self.bots[mat]
        self.time -= 1
        return self

    def build(self,bot):
        # check if you can build
        costs = blueprints[self.bp][bot]
        for mat in costs:
            if self.mats[mat] < costs[mat]: return False
            # # check if could have bought last round (bad bc could have bought something else)
            # if self.mats[mat] - self.bots[mat] >= costs[mat]: return False

        # check if you need to build
        largest_cost = 0
        if bot!=GEO:
            for recipe in blueprints[self.bp].values():
                largest_cost = max(largest_cost, recipe.get(bot,0))
            if self.bots[bot]==largest_cost: return False

        # build the robot
        for mat in costs:
            self.mats[mat] -= costs[mat]
        
        # self.harvest()
        self.time-=1
        self.bots[bot]+=1
        return True
    
    # find max possible geodes from this state
    def possible_geodes(self):
        return self.mats[GEO] + self.bots[GEO]*self.time + int((self.time*(self.time-1))/2)
    
    def score(self):
        return self.bots[GEO]*1000 + self.bots[OBS]*100 + self.bots[CLAY]*10 + self.bots[ORE]
    
    # # not needed due to use of copy.deepcopy
    # def __copy__(self):
    #     pass

quality_levels = defaultdict(int)
for bp in blueprints:
    max_geodes=0
    start = Inventory(bp)
    start.bots[ORE] = 1

    queue = deque([start])
    # print(start.possible_geodes())

    # while queue:
        
    #     new_queue = []
    #     for current in queue:
    #     # current = queue.popleft()
    #         # print(current.bots)
    #         max_geodes=max(max_geodes,current.mats[GEO])

    #         # can't catch best
    #         if current.possible_geodes() < max_geodes: continue

    #         # end of time
    #         if not current.time or current.time<0: continue
        
    #         # do nothing
    #         new = copy.deepcopy(current)
    #         new_queue.append(new.harvest())
            
    #         # build a bot
    #         for bot in materials:
    #             new = copy.deepcopy(current)
    #             if new.build(bot): new_queue.append(new)

    #     # sort and take best candidates
    #     new_queue.sort(key = lambda x: x.score(), reverse=True)
    #     queue = deque(new_queue[0:50000])

    # start.harvest()
    # start.harvest()
    # start.build(CLAY)
    # start.harvest()
    # start.build(CLAY)

    # start.harvest()
    # start.build(CLAY)
    # start.harvest()
    # start.harvest()
    # start.harvest()

    # start.build(OBS)
    # start.build(CLAY)
    # start.harvest()
    # start.harvest()
    # start.build(OBS)

    # start.harvest()
    # start.harvest()
    # start.build(GEO)
    # start.harvest()
    # start.harvest()

    # start.build(GEO)
    # start.harvest()
    # start.harvest()
    # start.harvest()

    # print(start.mats, start.time)

    while queue:
        current = queue.popleft()
        # print(current.bots)
        max_geodes=max(max_geodes,current.mats[GEO])

        # can't catch best
        if current.possible_geodes() < max_geodes: continue

        # end of time
        if not current.time or current.time<0: continue
    
        # do nothing
        new = copy.deepcopy(current)
        queue.append(new.harvest())
        
        # build a bot
        for bot in materials:
            new = copy.deepcopy(current)
            while new.time and not new.build(bot):
                new.harvest()
            queue.append(new)



    quality_levels[bp] = bp * max_geodes

print(quality_levels)