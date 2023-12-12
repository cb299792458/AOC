input = [l[:-1] for l in open('input.txt','r').readlines()]
from functools import cache

grand_total = 0
for line in input:
    record, groups = line.split(' ')

    # part 2
    record = '?'.join([record]*5)
    groups = ','.join([groups]*5)

    groups = groups.split(',')
    groups = [int(g) for g in groups]

    @cache
    def dp(record_idx, brokens, group_idx):        
        if record_idx==len(record):
            if not brokens and group_idx==len(groups):
                return 1
            elif group_idx==len(groups)-1 and brokens==groups[-1]:
                return 1
            else:
                return 0
        
        total = 0

        if record[record_idx] != '.':
            # add # to current group
            if group_idx<len(groups) and brokens<groups[group_idx]:
                total += dp(record_idx+1, brokens + 1, group_idx)
        
        if record[record_idx] != '#':
            # add . after #
            if group_idx<len(groups) and brokens==groups[group_idx]:
                total += dp(record_idx+1, 0, group_idx+1)
            # add . after .
            if brokens==0:
                total += dp(record_idx+1, 0, group_idx)
        
        return total
    
    grand_total += dp(0,0,0)
print(grand_total)