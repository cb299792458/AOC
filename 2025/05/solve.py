with open('input.txt', 'r') as f:
    blocks = f.read().strip().split("\n\n")

[ranges, ingredients] = blocks
ranges = ranges.split()
ingredients = ingredients.split()


fresh = 0
for ingredient in ingredients:
    num = int(ingredient)
    is_fresh = False
    for range in ranges:
        [s, e] = [int(n) for n in range.split('-')]
        if s <= num <= e:
            is_fresh = True
    if is_fresh:
        fresh += 1
    
print(fresh)
