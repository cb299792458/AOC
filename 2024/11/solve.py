from functools import cache
import math
input = [l[:-1] for l in open('input.txt','r').readlines()]

nums = list(map(int, input[0].split(' ')))

# # part 1
# for i in range(25):
#     new_nums = []
#     for num in nums:
#         if num == 0:
#             new_nums.append(1)
#         elif len(str(num))%2 == 0:
#             s = str(num)
#             new_nums.append(int(s[:len(s)//2]))
#             new_nums.append(int(s[len(s)//2:]))
#         else:
#             new_nums.append(2024*num)
#     nums = new_nums

# print(len(nums))

# part 2
def digits(num):
    return math.floor(math.log10(num)) + 1

def split(num):
    pow = 10 ** (digits(num)//2)
    return (num // pow, num % pow)

@cache
def get_stone_count(num, blinks):
    if blinks == 0:
        return 1
    
    if num == 0:
        return get_stone_count(1, blinks-1)

    if digits(num) % 2 == 0:
        (l, r) = split(num)
        return get_stone_count(l, blinks-1) + get_stone_count(r, blinks-1)
    
    return get_stone_count(2024*num, blinks-1)

print(sum([get_stone_count(num, 75) for num in nums]))
