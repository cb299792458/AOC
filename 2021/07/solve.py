input = [l[:-1] for l in open('input.txt','r').readlines()]
nums = [int(n) for n in input[0].split(',')]
print(nums)
print(sum(nums)/len(nums))

avg = 5

fuel = 0
for n in nums:
    fuel += abs(n-avg)
print(fuel)