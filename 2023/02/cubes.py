input = [l[:-1] for l in open('input.txt','r').readlines()]

# # part 1
# id_sum = 0
# limit = {
#     'red': 12,
#     'green': 13,
#     'blue': 14
# }

# for line in input:
#     [prefix, rounds] = line.split(':')
#     id = int(prefix.split(' ')[-1])
    
#     possible = True
#     for round in rounds.split(';'):
#         cubes = round.split(',')
#         for cube in cubes:
#             cube = cube.strip()
#             [num, color] = cube.split(' ')
#             num = int(num)
#             if num>limit[color]:
#                 possible = False
#     if possible:
#         id_sum += id
    
# print(id_sum)

# part 2
power_sum = 0
for line in input:
    [_, rounds] = line.split(':')
    
    limit = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for round in rounds.split(';'):

        cubes = round.split(',')
        for cube in cubes:
            cube = cube.strip()
            [num, color] = cube.split(' ')
            
            limit[color] = max(limit[color], int(num))

    power = limit['red']*limit['blue']*limit['green']
    power_sum += power
print(power_sum)


