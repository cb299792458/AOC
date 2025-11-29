input = [l[:-1] for l in open('input.txt','r').readlines()]
t = 0
def two_sum(nums, target):
    seen = set()
    for num in nums:
        if int(target) - int(num) in seen:
            return
        seen.add(int(num))
    
    # print(target)
    global t
    t = int(target)

for i in range(26, len(input)):
    two_sum(input[i-26:i], input[i])

for start in range(len(input)):
    for end in range(start, len(input)):
        nums = list(map(int, input[start:end]))
        # print(nums)
        if sum(nums) == t and end > start + 1:
            print(min(nums) + max(nums))
        if sum(nums) > t:
            break
