input = [l[:-1] for l in open('input.txt','r').readlines()]

nums1, nums2 = [], []
for line in input:
    [n1, n2] = line.split('   ')
    nums1.append(int(n1))
    nums2.append(int(n2))

nums1.sort()
nums2.sort()
dist = 0

for [n1, n2] in zip(nums1, nums2):
    dist += abs(n1 - n2)
print(dist)

from collections import Counter
counts2 = Counter(nums2)

similarity = 0
for n in nums1:
    similarity += counts2[n]*n
print(similarity)
