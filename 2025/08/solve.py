from collections import Counter
input = [l[:-1] for l in open('input.txt','r').readlines()]
boxes = [[int(n) for n in line.split(',')] for line in input]
N = len(boxes)

distances = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        (x1, y1, z1) = boxes[i]
        (x2, y2, z2) = boxes[j]

        dist = sum([
            (x1 - x2) ** 2,
            (y1 - y2) ** 2,
            (z1 - z2) ** 2,
        ])
        distances.append((dist, i, j))
distances.sort()

circuits = [n for n in range(N)]
for (_, i, j) in distances[:10000]:
    c1 = circuits[i]
    c2 = circuits[j]
    for k in range(N):
        if circuits[k] == c2:
            circuits[k] = c1
    
    if all([c == circuits[0] for c in circuits]):
        print(boxes[i][0] * boxes[j][0])
        break

counts = Counter(circuits)
vals = list(counts.values())
vals.sort(reverse=True)
# print(vals[0] * vals[1] * vals[2])
