calories = open('input.txt','r')
lines = calories.readlines()

sums = []
temp = []

for line in lines:
    line = line.replace('\n','')
    if not line:
        sums.append(sum(temp))
        temp = []
    else:
        temp.append(int(line))
    
# sums.sort(reverse=True)
sums.sort(key= lambda int : -int)

print(sum(sums[0:3]))