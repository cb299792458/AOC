from functools import cache
from time import time

input = [l[:-1] for l in open('input.txt','r').readlines()]
available = input[0].split(', ')
patterns = input[2:]

def possible(pattern, i):
    if i == len(pattern):
        return True
    
    for a in available:
        if pattern[i:i+len(a)] == a:
            if possible(pattern, i+len(a)):
                return True
    
    return False

@cache
def ways(pattern, i):
    if i == len(pattern):
        return 1
    
    res = 0
    for a in available:
        if pattern[i:i+len(a)] == a:
            res += ways(pattern, i+len(a))
    
    return res

@cache
def ways2(pattern):
    if pattern == '':
        return 1
    res = 0
    for a in available:
        if pattern[:len(a)] == a:
            res += ways2(pattern[len(a):])
    return res

curr = time()
part1 = 0
for pattern in patterns:
    if possible(pattern, 0):
        part1 += 1
print(part1, time()-curr)

curr = time()
part2 = 0
for pattern in patterns:
    part2 += ways(pattern, 0)
print(part2, time()-curr)

curr = time()
part2 = 0
for pattern in patterns:
    part2 += ways2(pattern)
print(part2, time()-curr)
