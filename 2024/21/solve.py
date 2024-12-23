input = [l[:-1] for l in open('input.txt','r').readlines()]

keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]
dpad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]
keypad_locations = dict()
dpad_locations = dict()
for r in range(4):
    for c in range(3):
        if keypad[r][c]:
            keypad_locations[keypad[r][c]] = (r, c)
for r in range(2):
    for c in range(3):
        if dpad[r][c]:
            dpad_locations[dpad[r][c]] = (r, c)

# print(keypad_locations)
# print(dpad_locations)

def keypad_to_dpad(keypad_input):
    keypad_r, keypad_c = keypad_locations['A']
    dpad_input = []
    for c in keypad_input:
        (next_r, next_c) = keypad_locations[c]
        while keypad_r < next_r:
            dpad_input.append('v')
            keypad_r += 1
        while keypad_r > next_r:
            dpad_input.append('^')
            keypad_r -= 1
        while keypad_c < next_c:
            dpad_input.append('>')
            keypad_c += 1
        while keypad_c > next_c:
            dpad_input.append('<')
            keypad_c -= 1
        dpad_input += 'A'
    return ''.join(dpad_input)

def dpad_to_dpad(input):
    (r, c) = dpad_locations['A']
    res = []
    for char in input:
        (nr, nc) = dpad_locations[char]
        while r < nr:
            res.append('v')
            r += 1
        while r > nr:
            res.append('^')
            r -= 1
        while c < nc:
            res.append('>')
            c += 1
        while c > nc:
            res.append('<')
            c -= 1
        res.append('A')
    return ''.join(res)

for line in input[:1]:
    print(line)
    code = keypad_to_dpad(line)
    print(code)
    for _ in range(3):
        code = dpad_to_dpad(code)
    print(code)
"""
v<A<A^>>Av<<A^>>AA<Av>AA^Av<<A^>>Av<A>A^AA<A>Av<A<AA^>>A<Av>AA^Av<A^>A<A>Av<A<AA^>>A<Av>AA^AAv<A<A^>>AvA^A<A>Av<<A^>>AvA^Av<A<A^>>Av<<A^>>A<Av>AA^AAAv<<A^>>Av<A>A^A<A>A
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>Av<<A>>^A<A>AvA<^AA>A<vAAA>^A<A^A>^^AvvvA
"""
