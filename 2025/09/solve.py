input = [l[:-1] for l in open('input.txt','r').readlines()]
nums = [[int(n) for n in line.split(',')] for line in input]
N = len(nums)

biggest = 0
for i in range(N):
    for j in range(i + 1, N):
        [x1, y1] = nums[i]
        [x2, y2] = nums[j]
        l = max(x1, x2) - min(x1, x2) + 1
        w = max(y1, y2) - min(y1, y2) + 1

        biggest = max(biggest, l * w)
print(biggest)
