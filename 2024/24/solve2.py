from collections import defaultdict, Counter
import random

input = open('input.txt', 'r').read().strip()
x, y, z = 'x', 'y', 'z' # dont do this
[start, gates] = input.split('\n\n')
start = start.split('\n')
gates = gates.split('\n')

outputs = []
parents = defaultdict(list)
children = defaultdict(list)
for line in gates:
    [p1, _, p2, _, output] = line.split(' ')
    outputs.append(output)
    parents[output].append(p1)
    parents[output].append(p2)
    children[p1].append(output)
    children[p2].append(output)

output_by_op = defaultdict(list)
z_ops = []
sums = []
carries = []
uses = defaultdict(Counter)
for line in gates:
    [p1, op, p2, _, output] = line.split(' ')
    output_by_op[op].append(output)
    if output[0] == 'z':
        z_ops.append((output, op))
    if op == 'XOR' and p1[0] == x and p2[0] == y:
        sums.append(output)
    if op == 'AND' and p1[0] == x and p2[0] == y:
        carries.append(output)
    uses[p1][op] += 1
    uses[p2][op] += 1

# this is some jank to look for outputs that don't match the same patter

bad_zs = [t[0] for t in z_ops if t[1] != 'XOR' and t[0] != 'z45']
# print(bad_zs)

bad_sums = [s for s in sums if (uses[s]['XOR'] != 1 or uses[s]['AND'] != 1) and s != 'z00']
# print(bad_sums)

bad_carries = [c for c in carries if uses[c]['AND'] == 1]
# print(bad_carries)

all_bads = bad_zs + bad_sums + bad_carries

def setup():
    wires = defaultdict(lambda: -1)
    for line in start:
        [key, val] = line.split(': ')
        wires[key] = int(val)
    return wires

def readZ(wires):
    res = 0
    for i in range(45):
        key = z + ('0' if i < 10 else '') + str(i)
        if wires[key] == -1:
            break
        res += wires[key] * (2 ** i)
        i+=1
    return res

def calculateZ(swaps, wires):
    updated = True
    while updated:
        updated = False
        for line in gates:
            [w1, op, w2, _, w3] = line.split(' ')
            if w3 in swaps:
                w3 = swaps[w3]

            if wires[w1] == -1 or wires[w2] == -1:
                continue
            if wires[w3] != -1:
                continue
            match op:
                case 'AND':
                    wires[w3] = wires[w1] & wires[w2]
                case 'OR':
                    wires[w3] = wires[w1] | wires[w2]
                case 'XOR':
                    wires[w3] = wires[w1] ^ wires[w2]
            updated = True
    return readZ(wires)

def input(char, num, wires):
    for i in range(45):
        key = char + ('0' if i < 10 else '') + str(i)
        wires[key] = num % 2
        num //= 2

swaps = {
    'tfn': 'cvh', 'cvh': 'tfn',
    'dbb': 'z23', 'z23': 'dbb',
    'hbk': 'z14', 'z14': 'hbk',
    'z18': 'kvn', 'kvn': 'z18',
}

# find possible swaps with an output from all_bads
# if there's no z involved, it's good
# if there is a z involved, it must swap with the output of an XOR
# trial and error bs abounds
for p in range(44):
    x_val = 2 ** p
    y_val = 2 ** p
    wires = setup()
    input(x, x_val, wires)
    input(y, y_val, wires)
    z_val = calculateZ({**swaps}, wires)
    if x_val + y_val != z_val:
        for o1 in all_bads:
            for o2 in outputs:
                if o1 == o2:
                    continue
                if o2 in all_bads:
                    continue
                wires = setup()
                input(x, x_val, wires)
                input(y, y_val, wires)
                z_val1 = calculateZ({**swaps, o1: o2, o2: o1}, wires)
                if x_val + y_val == z_val1:
                    print(o1,o2)
    else:
        print('good')

# check once four swaps are found
for _ in range(100):
    x_val = random.randint(0, 2 ** 44)
    y_val = random.randint(0, 2 ** 44)
    wires = setup()
    input(x, x_val, wires)
    input(y, y_val, wires)
    z_val = calculateZ({**swaps}, wires)
    if x_val + y_val != z_val:
        print('bad')
    else:
        print('good')

ans = list(swaps.keys())
ans.sort()
print(','.join(ans))
