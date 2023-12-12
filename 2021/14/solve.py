input = [l[:-1] for l in open('input.txt','r').readlines()]

polymer = input[0]
insert = dict()

for line in input[2:]:
    pair, new = line.split(' -> ')
    insert[pair] = new

for _ in range(10):
    curr = ''
    for i in range(len(polymer)-1):
        a,b = polymer[i], polymer[i+1]
        curr += a + insert[a+b]
    
    curr += polymer[-1]

    polymer = curr

from collections import Counter
print(Counter(polymer))

start = input[0]
polymer = Counter()
for i in range(len(start)-1):
    polymer[start[i:i+2]]+=1
# print(polymer)

for _ in range(40):
    curr = Counter()
    for key,num in polymer.items():
        a,c = key[0],key[1]
        b = insert[key]
        curr[a+b] += num
        curr[b+c] += num
    polymer = curr

# print(polymer)
final = Counter()
for key,val in polymer.items():
    d,e = key[0],key[1]
    final[d] += val
    final[e] += val

# all counted twice except first and last
final[input[0][0]] += 1
final[input[0][-1]] += 1

counts = list(final.values())
counts.sort()
print((counts[-1]-counts[0])/2)