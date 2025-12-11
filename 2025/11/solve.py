from functools import cache
from collections import defaultdict

lines = [l[:-1] for l in open('input.txt','r').readlines()]
connections = defaultdict(list)
parents = defaultdict(list)
for line in lines:
    [input, outputs] = line.split(': ')
    for output in outputs.split():
        connections[input].append(output)
        parents[output].append(input)

res = 0
def dfs(node):
    if node == 'out':
        global res
        res += 1
    for connection in connections[node]:
        dfs(connection)

dfs('you')
print(res)


@cache
def dfs2(node, saw_fft, saw_dac):
    if node == 'out':
        return 1 if saw_dac and saw_fft else 0
    res = 0
    for connection in connections[node]:
        res += dfs2(connection, saw_fft or node == 'fft', saw_dac or node == 'dac')
    return res

print(dfs2('svr', False, False))
