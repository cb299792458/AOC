from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]
adjs = defaultdict(set)

for line in input:
    [c1, c2] = line.split('-')
    adjs[c1].add(c2)
    adjs[c2].add(c1)

# # part 1
# threes = []

# for c1 in adjs:
#     if c1[0] == 't':
#         for c2 in adjs[c1]:
#             for c3 in adjs[c1]:
#                 if c2 != c3 and c3 in adjs[c2]:
#                     threes.append(tuple(sorted([c1, c2, c3])))

# print(len(set(threes)))

#  part 2
lans = []
for computer in adjs:
    for lan in lans:
        if all([computer in adjs[c] for c in lan]):
            lans.append(lan + [computer])
    lans.append([computer])
lans.sort(key=len, reverse=True)
lans[0].sort()
print(','.join(lans[0]))
