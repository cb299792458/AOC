input = [l[:-1] for l in open('input.txt','r').readlines()]

joltage = 0
for line in input:
    nums = [int(c) for c in line]
    first = max(nums[:-1])
    last = max(nums[nums.index(first)+1:])
    joltage += first * 10 + last

print(joltage)
