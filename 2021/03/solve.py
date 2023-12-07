input = [l[:-1] for l in open('input.txt','r').readlines()]
from collections import Counter
ROWS = len(input)
COLS = len(input[0])

def str_to_dec(string):
    res = 0
    for c in string:
        res *= 2
        if c=='1':
            res += 1
    return res

counts = [Counter() for _ in range(COLS)]
for row in input:
    for col, char in enumerate(row):
        counts[col][char]+=1

gamma = ['1' if count['1']>count['0'] else '0' for count in counts]
gamma = ''.join(gamma)
gamma = str_to_dec(gamma)
# print(gamma*((2**COLS)-gamma-1))

rows = input
i=0
while len(rows)>1:
    counts = Counter([row[i] for row in rows])
    common = '0' if counts['0'] > counts['1'] else '1'
    rows = [row for row in rows if row[i]==common]
    i+=1
oxygen=rows[0]

rows = input
i=0
while len(rows)>1:
    counts = Counter([row[i] for row in rows])
    common = '0' if counts['0'] <= counts['1'] else '1'
    rows = [row for row in rows if row[i]==common]
    i+=1
carbon=rows[0]

print(str_to_dec(oxygen)*str_to_dec(carbon))