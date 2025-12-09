from functools import cache
input = [l[:-1] for l in open('input.txt','r').readlines()]

# # part 1
# indices = set([input[0].index('S')])
# splits = 0
# for line in input[1:]:
#     new_indices = set()
#     for (i, c) in enumerate(line):
#         if i in indices:
#             if c == '^':
#                 new_indices.add(i-1)
#                 new_indices.add(i+1)
#                 splits += 1
#             else:
#                 new_indices.add(i)
#     indices = new_indices

# print(splits)

# part 2
R = len(input)
@cache
def backtrack(r, c):
    if r == R: # reached end
        return 1

    if input[r][c] == '.': # beam goes straight down
        return backtrack(r + 1, c)
    else: # beam splits to two adjacent columns, then travels down
        return backtrack(r + 1, c + 1) + backtrack(r + 1, c - 1)

# Start below the "S"
print(backtrack(1, input[0].index('S')))
