input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
import math

nums = [(int(input[i])*811589153,i) for i in range(len(input))]
moves = nums.copy()
# print(nums)
last_id = len(nums) - 1

# print(nums)
# print(len(nums),len(set(nums)))

for _ in range(10):
    for tup in moves:
        # index = nums.index(num)
        index = None
        for i in range(len(nums)):
            if nums[i]==tup:
                index=i
                break

        temp = nums.pop(index) # 1

        # if index+num<0: index+= math.floor((index+num)/length)
        # index = (index + num) % length 
        index+=tup[0]

        # while index<=0:
        #     index+=last_id
        # while index>last_id:
        #     index-=last_id
        index += last_id*((last_id-index)//last_id)

        nums = nums[0:index] + [temp] + nums[index:]

        # print(nums)




index_of_zero = None
for i in range(len(nums)):
    if nums[i][0]==0:
        index_of_zero=i
        break

i1,i2,i3 = index_of_zero+1000, index_of_zero+2000, index_of_zero+3000
print(sum([nums[i1%len(nums)][0],nums[i2%len(nums)][0],nums[i3%len(nums)][0]]))
