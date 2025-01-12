from collections import defaultdict, Counter
import random
input = open('input.txt', 'r').read().strip()

X, Y, Z = 'x', 'y', 'z'
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

wires = defaultdict(lambda: -1)
for line in start:
    [key, val] = line.split(': ')
    wires[key] = int(val)

def set_wires(dictionary):
    updated = True
    while updated:
        updated = False
        for line in gates:
            [w1, op, w2, _, w3] = line.split(' ')

            if dictionary[w1] == -1 or dictionary[w2] == -1:
                continue
            if dictionary[w3] != -1:
                continue
            match op:
                case 'AND':
                    dictionary[w3] = dictionary[w1] & dictionary[w2]
                case 'OR':
                    dictionary[w3] = dictionary[w1] | dictionary[w2]
                case 'XOR':
                    dictionary[w3] = dictionary[w1] ^ dictionary[w2]
            updated = True
# set_wires()

def read_num(char, wires): 
    res = 0
    i = 0
    while True:
        key = char + ('0' if i < 10 else '') + str(i)
        if wires[key] == -1:
            break
        res += wires[key] * (2 ** i)
        i+=1
    return res

def input(char, num, wires):
    for i in range(45):
        key = char + ('0' if i < 10 else '') + str(i)
        wires[key] = num % 2
        num //= 2

def to_binary(num):
    res = []
    for _ in range(46):
        res.append(num % 2)
        num //= 2
    return res

def genealogy(wire):
    res = []
    queue = [wire]
    while queue:
        curr = queue.pop(0)
        res.append(curr)
        queue.extend(parents[curr])
    return res
        
all_zeroes = defaultdict(lambda: -1)
input(X, 0, all_zeroes)
input(Y, 0, all_zeroes)
set_wires(all_zeroes)

for i in range(45):
    test_wires = defaultdict(lambda: -1)
    input(X, 2**i, test_wires)
    input(Y, 2**i, test_wires)
    set_wires(test_wires)

    if read_num(Z, test_wires) == 2**(i+1):
        # print('good')
        continue

    expected = 2**(i+1)
    actual = read_num(Z, test_wires)
    error1 = to_binary(expected).index(1)
    error2 = to_binary(actual).index(1)
    print('Error:', error1, error2)
    # g1 = genealogy(Z + str(error1))
    # g2 = genealogy(Z + str(error2))
    # print(list(set(g1) & set(g2)))

problems = ['z14','z15']
all_problems = list(set(genealogy('z14')) & set(genealogy('z15')))
def prune(list):
    originals = set(list)
    result = []
    for item in list:
        if all(child in originals for child in children[item]):
            continue
        # if all(parent in originals for parent in parents[item]):
        #     continue
        result.append(item)
    return result

all_problems = prune(all_problems)
print(all_problems)
