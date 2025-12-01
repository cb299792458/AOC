input = [l[:-1] for l in open('input.txt','r').readlines()]
N, S, W, E, L, R, F = 'N', 'S', 'W', 'E', 'L', 'R', 'F'

compass = {
    E: [0, 1],
    S: [1, 0],
    W: [0, -1],
    N: [-1, 0],
}
directions = list(compass.values())
di = 0

r, c = 0, 0

# # part 1
# for line in input:
#     char = line[0]
#     num = int(line[1:])

#     if char in [N, S, W, E]:
#         r += compass[char][0] * num
#         c += compass[char][1] * num
#     elif char == L:
#         di -= num // 90
#     elif char == R:
#         di += num // 90
#     elif char == F:
#         r += directions[di%4][0] * num
#         c += directions[di%4][1] * num
#     else:
#         raise Exception('unknown instruction')

# print(abs(r) + abs(c))

wr, wc = -1, 10
for line in input:
    char = line[0]
    num = int(line[1:])

    if char in [N, S, W, E]:
        wr += compass[char][0] * num
        wc += compass[char][1] * num
    elif char == R:
        for _ in range(num // 90):
            [wr, wc] = [wc, -wr]
    elif char == L:
        for _ in range(num // 90):
            [wr, wc] = [-wc, wr]
    elif char == F:
        r += wr * num
        c += wc * num
    else:
        raise Exception('unknown instruction')

print(abs(r) + abs(c))
