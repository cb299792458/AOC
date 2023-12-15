input = [l[:-1] for l in open('input.txt','r').readlines()]

def hash(s):
    val=0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

total = 0
for s in input[0].split(','):
    total += hash(s)
print(total)

boxes = [dict() for _ in range(256)]
for s in input[0].split(','):
    if '=' in s:
        [label, focal] = s.split('=')
        box = hash(label)
        boxes[box][label] = focal
    else:
        assert(s[-1]=='-')
        box = hash(s[:-1])
        if s[:-1] in boxes[box]:
            del boxes[box][s[:-1]]

power = 0
for box,hashmap in enumerate(boxes):
    for [slot, focal] in enumerate(hashmap.values()):
        power += (1+slot)*(1+box)*int(focal)

print(power)