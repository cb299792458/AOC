import math

input = [l[:-1] for l in open('input.txt','r').readlines()]
start = int(input[0])
ids = input[1].split(',')

least = math.inf
res = 0
for id in ids:
    if id =='x':
        continue
    id = int(id)
    prev = start % id

    wait = id - prev
    if wait < least:
        least = wait
        res = id * wait

print(res)

indices = dict()
for [i, s] in enumerate(ids):
    if s != 'x':
        indices[int(s)] = i

time = 0
step = 1

for (bus_id, index) in indices.items():
    while (time + index) % bus_id:
        time += step
    
    step *= bus_id

print(time)
