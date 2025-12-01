input = [l[:-1] for l in open('input.txt','r').readlines()]

pos = 50
zeroes = 0
for line in input:
    dir = line[0]
    num = int(line[1:])
    
    for _ in range(num):
        pos += 1 if dir == 'R' else -1
        pos %= 100

        if pos == 0:
            zeroes += 1

print(zeroes)
