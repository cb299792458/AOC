from collections import defaultdict
crates=open('input.txt','r').readlines()
crates=[a[:-1] for a in crates]

moves = crates[10:]
crates = crates[:9]
stacks = defaultdict(list)

# make stacks
for row in range(len(crates)-2,-1,-1):
    for col in range(1,len(crates[0]),4):
        if crates[row][col]!=' ': stacks[crates[-1][col]].append(crates[row][col])

# format moves
for move in moves:

    words = move.split(' ')
    num, start, end = int(words[1]),words[3],words[5]
    # print(num,start,end)

    # do moves
    while num:
        stacks[end].append(stacks[start].pop())
        num-=1

# print stacks
for i in range(1,10):
    print(i, stacks[str(i)][-1])
