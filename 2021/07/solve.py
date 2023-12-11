input = [l[:-1] for l in open('input.txt','r').readlines()]
nums = [int(n) for n in input[0].split(',')]
nums.sort()
median = nums[(len(nums)//2)]

fuel = 0
for n in nums:
    fuel += abs(n-median)
print(fuel)

mean = sum(nums)//len(nums)
fuel = 0
for n in nums:
    m = abs(n-mean)
    fuel += (m*(m+1))//2
print(fuel)