print( sum( [int(chars[0]+chars[-1]) for chars in [[char for char in line if char.isdigit()] for line in open('input.txt','r').readlines()]] ) )

input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

# # Part 1 (no one line)
# vals1 = []
# for line in input:
#     nums = [c for c in line if c.isdigit()]
#     vals1.append(int(nums[0]+nums[-1]))
# print(sum(vals1))

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
vals2 = []

for line in input:
    nums=[]
    for i, char in enumerate(line):
        if char.isdigit():
            nums.append(int(char))
        else:
            for j, word in enumerate(words):
                if word == line[i:i+len(word)]:
                    nums.append(j+1)
    vals2.append(10*nums[0]+nums[-1])     

print(sum(vals2)) 
