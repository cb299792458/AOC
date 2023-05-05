from collections import deque
monkeys=[
    [83,97,95,67,],
    [71,70,79,88,56,70,],
    [98,51,51,63,80,85,84,95,],
    [77,90,82,80,79,],
    [68,],
    [60,94,],
    [81,51,85,],
    [98,81,63,65,84,71,84,],
]

# monkeys=[
#     [83,],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
# ]

# monkeys=[
#     [79,98],
#     [54,65,75,74],
#     [79,60,97],
#     [74]
# ]

for i in range(len(monkeys)):
    monkeys[i]=deque(monkeys[i])
inspections=[0]*len(monkeys)

nums=[
    [lambda n: n*19,17,2,7],
    [lambda n: n+2,19,7,0],
    [lambda n: n+7,7,4,3],
    [lambda n: n+1,11,6,4],
    [lambda n: n*5,13,6,5],
    [lambda n: n+5,3,1,0],
    [lambda n: n*n,5,5,1],
    [lambda n: n+3,2,2,3],
]

# nums=[
#     [lambda n: n*19,23,2,3],
#     [lambda n: n+6,19,2,0],
#     [lambda n: n*n,13,1,3],
#     [lambda n: n+3,17,0,1],
# ]




for _ in range(10000):
    for i in range(len(monkeys)):
        while monkeys[i]:
            inspections[i]+=1
            item = monkeys[i].pop()
            item = nums[i][0](item)
            # item = item // 3
            item = item % (17*19*7*11*13*3*5*2)
            (monkeys[nums[i][2]] if item%nums[i][1]==0 else monkeys[nums[i][3]]).append(item)
            # print(item)
print(sorted(inspections)[-1]*sorted(inspections)[-2])