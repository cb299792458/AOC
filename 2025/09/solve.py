input = [l[:-1] for l in open('input.txt','r').readlines()]
nums = [[int(n) for n in line.split(',')] for line in input]
N = len(nums)

# # part 1
# biggest = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         [x1, y1] = nums[i]
#         [x2, y2] = nums[j]
#         l = max(x1, x2) - min(x1, x2) + 1
#         w = max(y1, y2) - min(y1, y2) + 1

#         biggest = max(biggest, l * w)
# print(biggest)

# part 2
horis = []
verts = []
for i in range(N):
    [r1, c1] = nums[i]
    [r2, c2] = nums[i - 1]

    if r1 == r2:
        horis.append([r1, min(c1, c2), max(c1, c2)])
    elif c1 == c2:
        verts.append([c2, min(r1, r2), max(r1, r2)])
    else:
        raise Exception('uh oh')

def overlaps(r1, c1, r2, c2) -> bool:
    if r1 > r2:
        return overlaps(r2, c1, r1, c2)
    if c1 > c2:
        return overlaps(r1, c2, r2, c1)

    # horizontal walls
    for row, lo, hi in horis:
        if r1 < row < r2:
            if max(c1, lo) < min(c2, hi):
                return True

    # vertical walls
    for col, lo, hi in verts:
        if c1 < col < c2:
            if max(r1, lo) < min(r2, hi):
                return True

    return False

biggest = 0
for i in range(N):
    for j in range(i + 1, N):
        [x1, y1] = nums[i]
        [x2, y2] = nums[j]

        if overlaps(x1, y1, x2, y2):
            continue

        l = max(x1, x2) - min(x1, x2) + 1
        w = max(y1, y2) - min(y1, y2) + 1

        biggest = max(biggest, l * w)
print(biggest)