input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

vals1 = []
for line in input:
    nums = [c for c in line if c.isdigit()]
    vals1.append(int(nums[0]+nums[-1]))
print(sum(vals1))

words = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
vals2 = []

for line in input:
    i=0
    nums=[]
    while i<len(line):
        if line[i].isdigit():
            nums.append(line[i])
        else:
            for j in range(1,10):
                word = words[j]
                if word == line[i:i+len(word)]:
                    nums.append(str(j))
        i+=1
    vals2.append(int(nums[0]+nums[-1]))     

print(sum(vals2)) 
        