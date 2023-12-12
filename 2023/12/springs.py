input = [l[:-1] for l in open('input.txt','r').readlines()]

arrangements = 0

def check(springs, damaged):
    springs = springs.split('.')
    springs = [s for s in springs if s!='']
    springs = [len(s) for s in springs]
    return springs == damaged

def dfs(path, record, groups):
    i = len(path)

    if i==len(record):
        if check(path, groups):
            global arrangements
            arrangements += 1
        return
    
    if record[i]!='.':
        dfs(path+'#', record, groups)
    if record[i]!='#':
        dfs(path+'.', record, groups)


for line in input:
    record, groups = line.split(' ')
    
    # record = '?'.join([record]*5)
    # groups = ','.join([groups]*5)
    
    groups = groups.split(',')
    groups = [int(g) for g in groups]

    dfs('', record, groups)

print(arrangements)