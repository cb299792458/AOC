input = [l[:-1] for l in open('input.txt','r').readlines()]
from functools import cache

"""
record: full record from input
curr: current record (actual)
broken: current streak of broken springs
groups: unfinished groups of broken springs
"""

@cache
def ways(record, curr, broken, groups):
    # print('called with', record, curr, broken, groups)

    # base case
    if len(curr)==len(record):
        if groups==() and not broken:
            # print('got 1')
            return 1
        else:
            # print('got 0')
            return 0

    res = 0

    #a: try adding #
    if record[len(curr)]!='.':
        if curr and curr[-1]=='#' and broken==0:
            pass
        else:

            new_curr = curr + '#'
            new_broken = broken + 1
            if groups and new_broken==groups[0]:
                res += ways(record, new_curr, 0, groups[1:])
            else:
                res += ways(record, new_curr, new_broken, groups)

    #b: try adding .
    if record[len(curr)]!='#':
        new_curr = curr + '.'
        new_broken = 0
        new_groups = groups

        if broken:
            if groups and groups[0]==broken:
                new_groups = groups[1:]
            else:
                # print('got', res)
                return res
        res += ways(record, new_curr, new_broken, new_groups)
    
    # print('got', res)
    return res

total = 0
for line in input:

    record, groups = line.split(' ')
    
    # # part 2
    # record = '?'.join([record]*5)
    # groups = ','.join([groups]*5)
    
    groups = groups.split(',')
    groups = tuple([int(g) for g in groups])

    total += ways(record, '', 0, groups)
print(total)
