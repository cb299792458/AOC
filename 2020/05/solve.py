input = [l[:-1] for l in open('input.txt','r').readlines()]

ids = set()
lowest = 10 ** 20
highest = 0

for seat in input:
    r = 0
    for char in seat[:-3]:
        r *= 2
        if char == 'B':
            r += 1
    
    c = 0
    for char in seat[-3:]:
        c *= 2
        if char == 'R':
            c += 1
    
    id = 8 * r + c
    ids.add(id)
    highest = max(highest, id)
    lowest = min(lowest, id)

# print(highest, lowest)
for n in range(lowest, highest):
    if n not in ids:
        print(n)
