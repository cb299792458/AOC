from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]

prereqs = defaultdict(list)
i = 0
while input[i] != '':
    a,b = input[i].split('|')
    prereqs[b].append(a)
    i += 1

i += 1
total = 0
total2 = 0

while i < len(input):
    valid = True
    pages = input[i].split(',')

    cant = set()
    for page in pages:
        if page in cant:
            valid = False
            break
        for p in prereqs[page]:
            cant.add(p)
    
    if valid: # part 1
        total += int(pages[len(pages)//2])
    else: # part 2
        ordered = []
        while len(ordered) < len(pages):
            for page in pages:
                if page in ordered:
                    continue
                if all((p in ordered or p not in pages) for p in prereqs[page]):
                    ordered.append(page)
                    break
        total2 += int(ordered[len(ordered)//2])

    i+= 1
print(total)
print(total2)
    
