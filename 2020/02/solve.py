from collections import Counter
input = [l[:-1] for l in open('input.txt','r').readlines()]

valid = 0
part2 = []
for line in input:
    [nums, char, string] = line.split(' ')
    [least, most] = map(int, nums.split('-'))
    char = char[0]

    counts = Counter(string)
    if counts[char] >= least and counts[char] <= most:
        valid += 1
        
    curr = 0
    if string[least - 1] == char:
        curr += 1
    if string[most - 1] == char:
        curr += 1
    
    part2.append(curr)

print(len([p for p in part2 if p == 1]))
