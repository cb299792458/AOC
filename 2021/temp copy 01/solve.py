input = [l[:-1] for l in open('input.txt','r').readlines()]
input = input + [0]

increases = 0
for i, depth in enumerate(input[:-1]):
  if int(depth)<int(input[i+1]):
    increases+=1
print(increases)

input = input + [0]
increases = 0
for i, depth in enumerate(input[:-3]):
  if int(depth)<int(input[i+3]):
    increases+=1
print(increases)