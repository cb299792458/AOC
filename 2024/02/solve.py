input = [l[:-1] for l in open('input.txt','r').readlines()]

safes = 0

def is_safe(levels):
    inc = False
    dec = False

    for i in range(1, len(levels)):
        [curr, prev] = [levels[i], levels[i-1]]
        if curr > prev:
            inc = True
        elif curr < prev:
            dec = True
        if abs(curr - prev) < 1 or abs(curr - prev) > 3:
            return False
    return inc ^ dec

for report in input:
    levels = list(map(int, report.split(' ')))
    if is_safe(levels):
        safes += 1

print(safes)

safes = 0

for report in input:
    levels = list(map(int, report.split(' ')))
    any_safe = False
    for i in range(len(levels)):
        skipped = levels[:i] + levels[i+1:]
        if is_safe(skipped):
            any_safe = True
    
    if any_safe:
        safes += 1
print(safes)
