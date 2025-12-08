import math
input = [l[:-1] for l in open('input.txt','r').readlines()]

# # part 1
# grid = [[int(s) for s in line.split()] for line in input[:-1]]
# ops = [c for c in input[-1].split()]
# R, C = len(grid), len(ops)

# total = 0
# for c in range(C):
#     if ops[c] == '+':
#         total += sum(grid[r][c] for r in range(R))
#     else:
#         product = 1
#         for r in range(R):
#             product *= grid[r][c]
#         total += product

# print(total)

# part 2
grid = [[c for c in line] for line in input[:-1]]
ops = [c for c in input[-1].split()]
R, C = len(grid), len(grid[0])
op_idx = 0
nums = []
total = 0

def handle():
    global op_idx, nums, total
    op = ops[op_idx]
    if op == '+':
        for num in nums:
            total += num
    else:
        subtotal = 1
        for num in nums:
            subtotal *= num
        total += subtotal
    
    op_idx += 1
    nums = []

for c in range(C):
    digits = [grid[r][c] for r in range(R)]
    if all(d == ' ' for d in digits):
        handle()
    else:
        num = ''
        for d in digits:
            num += d if d != ' ' else ''
        nums.append(int(num))
handle()

print(total)
