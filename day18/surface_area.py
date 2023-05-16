input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

points = [(int(num) for num in line.split(',')) for line in input]
points = [tuple(l) for l in points]
# print(points)

dirs=(
    (1,0,0),
    (-1,0,0),
    (0,1,0),
    (0,-1,0),
    (0,0,1),
    (0,0,-1),
)

sa=0
cubes=set(points)
seen=set()


# # dfs search
# def explore(tup):
#     global sa
#     if tup in seen: return False

#     seen.add(tup)

#     for d in dirs:
#         # check all 6 directions
#         new=(tup[0]+d[0],tup[1]+d[1],tup[2]+d[2])

#         if new not in cubes: sa+=1
#         else: explore(new)

# for pt in points:
#     explore(pt)
# print(sa)


sa=6*len(cubes)
for tup in points:
    # global sa
    for d in dirs:
        # check all 6 directions
        new=(tup[0]+d[0],tup[1]+d[1],tup[2]+d[2])

        if new in cubes: sa-=1
print(sa)