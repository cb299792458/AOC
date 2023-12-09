input = [l[:-1] for l in open('input.txt','r').readlines()]
start = [int(n) for n in input[0].split(',')]
# print(start)

fish = start
for _ in range(80):
    new_fish = []
    for f in fish:
        if f:
            new_fish.append(f-1)
        else:
            new_fish.append(6)
            new_fish.append(8)
    fish=new_fish
print(len(fish))

from collections import Counter, defaultdict
fish = Counter(start)
for _ in range(256):
    new_fish = defaultdict(int)
    for n in range(1,9):
        new_fish[n-1] = fish[n]
    new_fish[6] += fish[0]
    new_fish[8] += fish[0]
    fish = new_fish
print(fish)
print(sum(fish.values()))