from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]

divider = input.index('')

workflows = defaultdict(list)
for line in input[:divider]:
    name = line[:line.find('{')]
    rules = line[line.find('{')+1:-1].split(',')
    for r in rules[:-1]:
        rule, dest = r.split(':')
        workflows[name].append((rule, dest))
    workflows[name].append((None, rules[-1]))

def check(rule, part):
    if not rule:
        return True
    key, comp, num = rule[0], rule[1], int(rule[2:])
    if comp=='<':
        return part[key]<num
    elif comp=='>':
        return part[key]>num
    else:
        print('uh oh spaghettios')

# # part 1
# parts = []
# for line in input[1+divider:]:
#     part = {}
#     ratings = line[1:-1].split(',')
#     for rating in ratings:
#         k,v = rating.split('=')
#         part[k] = int(v)
#     parts.append(part)

R, A = 'R', 'A'
x,m,a,s = 'x','m','a','s'
# results = {R: [], A: []}
# for part in parts:
#     rules = workflows['in']
#     finished = False

#     while not finished:
#         for rule,dest in rules:
#             if check(rule,part):
#                 if dest in [A,R]:
#                     results[dest].append(part)
#                     finished = True
#                 else:
#                     rules = workflows[dest]
#                 break

# total = 0
# for part in results[A]:
#     total += sum(part.values())
# print(total)

# part 2

adjs = defaultdict(list)
for [name, rules] in workflows.items():
    for i, (_, dest) in enumerate(rules):
        adjs[name].append((i,dest))

paths = []
def trace(path):
    curr = path[-1][1]
    if curr==A:
        paths.append(path)
    for adj in adjs[curr]:
        trace(path+[adj])
trace([(0, 'in')])

combos = 0
for path in paths:
    ranges = {
        x: [1,4000],
        m: [1,4000],
        a: [1,4000],
        s: [1,4000]
    }
    for i, (_, name) in enumerate(path[:-1]):
        (j, next) = path[i+1]

        for k, (rule, dest) in enumerate(workflows[name]):
            
            if k!=j: # don't match rule
                if rule:
                    key, comp, num = rule[0], rule[1], int(rule[2:])
                    if comp=='<':
                        ranges[key][0] = max(num, ranges[key][0])
                    elif comp=='>':
                        ranges[key][1] = min(num, ranges[key][1])
            
            else: # match rule, move on
                if rule:
                    key, comp, num = rule[0], rule[1], int(rule[2:])
                    if comp=='<':
                        ranges[key][1] = min(num-1, ranges[key][1])
                    elif comp=='>':
                        ranges[key][0] = max(num+1, ranges[key][0])
                break

    new_combos = 1
    for [small,large] in ranges.values():
        new_combos *= large-small+1
    combos += new_combos

print(combos)