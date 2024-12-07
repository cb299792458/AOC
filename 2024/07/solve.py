input = [l[:-1] for l in open('input.txt','r').readlines()]

def possibilities(nums):
    if len(nums) == 1:
        return set(nums)
    res = set()
    prev = possibilities(nums[:-1])
    for n in prev:
        res.add(n + nums[-1])
        res.add(n * nums[-1])

        # part 2
        res.add(int(str(n) + str(nums[-1])))

    return res

test_value_sum = 0

for line in input:
    [tv, nums] = line.split(': ')
    tv = int(tv)
    nums = list(map(int, nums.split(' ')))
    if tv in possibilities(nums):
        test_value_sum += tv
print(test_value_sum)
