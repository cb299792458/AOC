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
    inputs = ['']
    for c in keypad_input:
        new_inputs = []
        (next_r, next_c) = keypad_locations[c]
        vert = 'v' * (next_r-keypad_r) if next_r > keypad_r else '^' * (keypad_r-next_r)
        hori = '>' * (next_c-keypad_c) if next_c > keypad_c else '<' * (keypad_c-next_c)
        for i in inputs:
            if keypad_c == 0 and next_r == 3:
                pass
            else:
                new_inputs.append(i + vert + hori + 'A')
            if keypad_r == 3 and next_c == 0:
                pass
            else:
                new_inputs.append(i + hori + vert + 'A')
        
        inputs = set(new_inputs)
        keypad_r, keypad_c = next_r, next_c
    return inputs

def dpad_to_dpad(prev_inputs):
    all_results = []
    for input in prev_inputs:
        (r, c) = dpad_locations['A']
        results = ['']
        for char in input:
            new_results = []
            (next_r, next_c) = dpad_locations[char]
            vert = 'v' * (next_r-r) if next_r > r else '^' * (r-next_r)
            hori = '>' * (next_c-c) if next_c > c else '<' * (c-next_c)
            for result in results:
                if next_c == 0 and r == 0:
                    pass
                else:
                    new_results.append(result + vert + hori + 'A')
                if next_r == 0 and c == 0:
                    pass
                else:
                    new_results.append(result + hori + vert + 'A')
            results = set(new_results)
            r, c = next_r, next_c
        all_results.extend(results)
    return set(all_results)

complexities = 0
for line in input:
    num = int(line[:-1])
    inputs = dpad_to_dpad(dpad_to_dpad(keypad_to_dpad(line)))
    complexities += min(len(i) for i in inputs) * num
print(complexities)
