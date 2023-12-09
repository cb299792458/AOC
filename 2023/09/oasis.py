input = [l[:-1] for l in open('input.txt','r').readlines()]

new_nums = []
prev_nums = []

for line in input:
    nums = [int(n) for n in line.split()]
    seqs = [nums]

    while not all(n==0 for n in seqs[-1]):
        diffs = []
        for i in range(len(seqs[-1])-1):
            diffs.append(seqs[-1][i+1]-seqs[-1][i])
        seqs.append(diffs)
    
    seqs[-1].append(0)
    for i in range(len(seqs)-2,-1,-1):
        seqs[i].append(seqs[i][-1]+seqs[i+1][-1])

        seqs[i] = [seqs[i][0]-seqs[i+1][0]] + seqs[i]

    new_nums.append(seqs[0][-1])
    prev_nums.append(seqs[0][0])

print(sum(new_nums))
print(sum(prev_nums))