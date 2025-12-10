from collections import defaultdict, deque
import math

input = [l[:-1] for l in open('input.txt','r').readlines()]

all_lights = []
all_buttons = []
all_joltages = []

for line in input:
    parts = line.split()

    lights = parts[0][1:-1]
    lights = tuple(l == '#' for l in lights)
    all_lights.append(lights)

    buttons = parts[1:-1]
    buttons = [b[1:-1] for b in buttons]
    buttons = [[int(n) for n in b.split(',')] for b in buttons]
    all_buttons.append(buttons)

    joltages = parts[-1][1:-1]
    joltages = tuple(int(j) for j in joltages.split(','))
    all_joltages.append(joltages)

# # part 1
# total = 0
# for [lights, buttons] in zip(all_lights, all_buttons):
#     memo = defaultdict(lambda: math.inf)
#     N = len(lights)

#     # bfs
#     queue = deque([((False,) * N, 0)])

#     while queue:
#         [state, presses] = queue.popleft()

#         if memo[state] <= presses:
#             continue
#         memo[state] = presses

#         for button in buttons:
#             new_state = tuple(not state[i] if i in button else state[i] for i in range(N))
#             queue.append((new_state, presses + 1))
    
#     total += memo[lights]

# print(total)

# part 2
total = 0
for [joltages, buttons] in zip(all_joltages, all_buttons):
    memo = defaultdict(lambda: math.inf)
    N = len(joltages)

    # bfs
    queue = deque([((0,) * N, 0)])

    while queue:
        [state, presses] = queue.popleft()

        if memo[state] <= presses:
            continue
        memo[state] = presses
        if any([state[i] > joltages[i] for i in range(N)]):
            continue


        for button in buttons:
            new_state = tuple(state[i] + 1 if i in button else state[i] for i in range(N))
            queue.append((new_state, presses + 1))
    
    total += memo[joltages]
    print(total)

print(total)

