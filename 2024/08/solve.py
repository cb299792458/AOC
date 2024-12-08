from collections import defaultdict

input = [l[:-1] for l in open('input.txt','r').readlines()]
M,N = len(input),len(input[0])

antennaes = defaultdict(list)
for r in range(M):
    for c in range(N):
        if input[r][c] != '.':
            antennaes[input[r][c]].append((r,c))

antinodes = set()
for ants in antennaes.values():
    for i in range(len(ants)):
        for j in range(i+1,len(ants)):
            a1, a2 = ants[i], ants[j]
            dr, dc = a2[0]-a1[0], a2[1]-a1[1]

            # # part 1
            # antinodes.add((a2[0]+dr,a2[1]+dc))
            # antinodes.add((a1[0]-dr,a1[1]-dc))

            # part 2
            (pr, pc) = a1
            while 0 <= pr < M and 0 <= pc < N:
                antinodes.add((pr,pc))
                pr -= dr
                pc -= dc
            (pr, pc) = a2
            while 0 <= pr < M and 0 <= pc < N:
                antinodes.add((pr,pc))
                pr += dr
                pc += dc

# # part 1
# antinodes_in_bounds = 0
# for (r,c) in antinodes:
#     if 0 <= r < M and 0 <= c < N:
#         antinodes_in_bounds += 1
# print(antinodes_in_bounds)

# part 2
print(len(antinodes))
