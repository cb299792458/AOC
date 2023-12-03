input = [l[:-1] for l in open('input.txt','r').readlines()]

ROWS = len(input)
COLS = len(input[0])
from collections import defaultdict

valid = set()
gears = []
gear_near = {}
gear_ratios = defaultdict(list)

for r, row in enumerate(input):
    for c, char in enumerate(row):
        if not char.isdigit() and char != '.':
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr, nc = r+dr, c+dc
                    if -1<nr<ROWS and -1<nc<COLS:
                        valid.add((nr,nc))

        if char=='*':
            gears.append((r,c))
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr, nc = r+dr, c+dc
                    if -1<nr<ROWS and -1<nc<COLS:
                        gear_near[(nr,nc)] = (r,c)
            

parts = []
for r, row in enumerate(input):
    c=-1
    while c<COLS-1:
        c+=1
        num = ''
        num_valid = False
        gear = None

        if input[r][c].isdigit():
            while c<COLS and input[r][c].isdigit():
                num += input[r][c]
                if (r,c) in valid:
                    num_valid = True

                if (r,c) in gear_near.keys():
                    gear = gear_near[(r,c)]

                c+=1
            if num_valid:
                parts.append(int(num))
            
            if gear:
                gear_ratios[gear].append(int(num))


print(sum(parts))

ratio_sum = 0
for ratios in gear_ratios.values():
    if len(ratios) != 2:
        continue
    ratio_sum +=ratios[0]*ratios[1]
print(ratio_sum)