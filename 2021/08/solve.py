data = [l[:-1] for l in open('input.txt','r').readlines()]

# # part 1
# instances = 0
# for line in data:
#     _, output = line.split(' | ')
#     segments = output.split(' ')
#     for segment in segments:
#         if len(segment) in [2,4,3,7]:
#             instances += 1
# print(instances)

# part 2
vals = []
for line in data:
    str_to_num = dict()
    num_to_str = dict()
    segments = [seg for seg in line.split(' ') if seg != '|']

    for segment in segments:
        segment = ''.join(sorted(list(segment)))
        l = len(segment)
        
        if l==2:
            str_to_num[segment]='1'
            num_to_str['1'] = segment
        if l==3:
            str_to_num[segment]='7'
            num_to_str['7'] = segment
        if l==4:
            str_to_num[segment]='4'
            num_to_str['4'] = segment
        if l==7:
            str_to_num[segment]='8'
            num_to_str['8'] = segment

    for segment in segments:
        segment = ''.join(sorted(list(segment)))
        l = len(segment)

        if l==6:
            six = False
            for c in num_to_str['1']:
                if c not in segment:
                    six = True
            if six:
                str_to_num[segment] = '6'
                num_to_str['6'] = segment
            else:
                zero = False
                for c in num_to_str['4']:
                    if c not in segment:
                        zero = True
                if zero:
                    str_to_num[segment] = '0'
                    num_to_str['0'] = segment
                else:
                    str_to_num[segment] = '9'
                    num_to_str['9'] = segment
 
    for segment in segments:
        segment = ''.join(sorted(list(segment)))
        l = len(segment)       
    
        if l==5:
            three = True
            for c in num_to_str['1']:
                if c not in segment:
                    three = False
            if three:
                str_to_num[segment] = '3'
                num_to_str['3'] = segment
            else:
                two = False
                for c in segment:
                    if c not in num_to_str['6']:
                        two = True
                if two:
                    str_to_num[segment] = '2'
                    num_to_str['2'] = segment
                else:
                    str_to_num[segment] = '5'
                    num_to_str['5'] = segment

    _, output = line.split(' | ')
    segments = output.split(' ')

    temp = []
    for segment in segments:
        segment = ''.join(sorted(list(segment)))
        temp.append(str_to_num[segment])
    vals.append(int(''.join(temp)))
print(sum(vals))