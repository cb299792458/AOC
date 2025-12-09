with open('input.txt', 'r') as f:
    blocks = f.read().strip().split("\n\n")

[ranges, ingredients] = blocks
ranges = ranges.split()
ingredients = ingredients.split()

# # part 1
# fresh = 0
# for ingredient in ingredients:
#     num = int(ingredient)
#     is_fresh = False
#     for range in ranges:
#         [s, e] = [int(n) for n in range.split('-')]
#         if s <= num <= e:
#             is_fresh = True
#     if is_fresh:
#         fresh += 1
    
# print(fresh)

# part 2
ranges = [line.split('-') for line in ranges]
ranges = [(int(a), int(b)) for [a, b] in ranges]
ranges.sort(key=lambda a: a[0])

stack = [ranges[0]]
for (s2, e2) in ranges[1:]:
    (s1, e1) = stack[-1]

    if s2 > e1:
        stack.append((s2, e2))
    else:
        stack[-1] = (s1, max(e1, e2))

# print(stack)
fresh = 0

for (s, e) in stack:
    fresh += e + 1 - s

print(fresh)
