rucksacks = open('input.txt','r').readlines()
rucksacks = [sack[:-1] for sack in rucksacks]
# print(rucksacks)

letters = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = dict()
for i in range(1,len(letters)):
    priorities[letters[i]]=i
# print(priorities)

sum=0
# for sack in rucksacks:
#     first,second = sack[:int(len(sack)/2)],sack[int(len(sack)/2):]

#     first = set(first)
#     for item in second:
#         if item in first:
#             sum += priorities[item]
#             break

groups = [[rucksacks[i],rucksacks[i+1],rucksacks[i+2]] for i in range(0,len(rucksacks),3)]

for group in groups:
    i1,i2,i3 = set(group[0]),set(group[1]),set(group[2]),
    items = i1.intersection(i2,i3)

    # print(list(items))
    sum+=priorities[list(items)[0]]

print(sum)
