from functools import cache
input = [l[:-1] for l in open('input.txt','r').readlines()]
input = [[int(c) for c in line] for line in input]

N = len(input[0])
# joltage = 0
# for line in input:
#     nums = [int(c) for c in line]
#     first = max(nums[:-1])
#     last = max(nums[nums.index(first)+1:])
#     joltage += first * 10 + last

# print(joltage)

joltage = 0
for line in input:
    @cache
    def dp(index, digits): # index goes backwards from N - 1 to 0
        if index == -1: # llegue al comienzo de la linea
            return 0
        if digits == 12: # ya tiene 12 digitos
            return 0
        
        skip = dp(index - 1, digits)
        take = 10 * dp(index - 1, digits + 1) + line[index]
        
        return max(skip, take)
    
    joltage += dp(N - 1, 0)
print(joltage)
