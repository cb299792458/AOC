from collections import Counter
input = [l[:-1] for l in open('input.txt','r').readlines()]
input = list(map(int, input))

input.sort()
input.append(input[-1] + 3)

prev = 0
diffs = Counter()
for num in input:
    diffs[num - prev] += 1
    prev = num

print(diffs[1] * diffs[3])

ways = Counter()
ways[0] = 1
for num in input:
    ways[num] = ways[num-1] + ways[num-2] + ways[num-3]
print(ways[input[-1]])
