input = [l[:-1] for l in open('input.txt','r').readlines()]
horizontal = 0
depth = 0

for line in input:
  direction, num = line.split()
  num = int(num)

  if direction=='forward':
    horizontal += num
  if direction=='down':
    depth += num
  if direction=='up':
    depth -= num

print(horizontal*depth)

horizontal = 0
depth = 0
aim = 0
for line in input:
  direction, num = line.split()
  num = int(num)

  if direction=='forward':
    horizontal += num
    depth += aim*num
  if direction=='down':
    aim += num
  if direction=='up':
    aim -= num

print(horizontal*depth)