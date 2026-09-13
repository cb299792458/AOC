from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]
input = input[1]
input = [int(n) for n in input.split(',')]

last_spoken = defaultdict(list)
turn = 0

nums = []

while turn < 30000000:
    if turn < len(input):
        curr = input[turn]
    else:
        last_num = nums[-1]

        if len(last_spoken[last_num]) < 2:
            curr = 0
        else:
            curr = last_spoken[last_num][-1] - last_spoken[last_num][-2]

    nums.append(curr)
    last_spoken[curr].append(turn)
    turn += 1

print(nums[-1])