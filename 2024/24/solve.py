from collections import defaultdict
input = open('input.txt', 'r').read().strip()

[start, gates] = input.split('\n\n')
start = start.split('\n')
gates = gates.split('\n')

wires = defaultdict(lambda: -1)
for line in start:
    [key, val] = line.split(': ')
    wires[key] = int(val)

updated = True
while updated:
    updated = False
    for line in gates:
        [w1, op, w2, _, w3] = line.split(' ')

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

def read_num(char):
    res = 0
    i = 0
    while True:
        key = char + ('0' if i < 10 else '') + str(i)
        if wires[key] == -1:
            break
        res += wires[key] * (2 ** i)
        i+=1
    return res
print(read_num('z'))
