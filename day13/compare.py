input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

def compare(a,b):
    # print(f'comparing {a} and {b}')
    if isinstance(a,int) and isinstance(b,int):
        if a==b: return "same"
        return a<b
    
    if isinstance(a,list) and isinstance(b,list):
        for i in range(max(len(a),len(b))):
            if i==len(a): return True
            if i==len(b): return False
            
            if compare(a[i],b[i])=='same': continue
            if compare(a[i],b[i])==True: return True
            if compare(a[i],b[i])==False: return False

        return 'same'
    
    if isinstance(a,int):
        return compare([a],b)
    else:
        return compare(a,[b])
    

all_lines=[[[2]],[[6]]]
all_lines=[]

sum=0
index=0

for i in range(0,len(input),3):
    index+=1
    a=eval(input[i])
    b=eval(input[i+1])
    all_lines.append(a)
    all_lines.append(b)
    if compare(a,b)==True:
        sum+=index

left=1
right=1

for l in all_lines:
    if compare([[2]],l)==False:
        left += 1
        right+=1
    elif compare([[6]],l)==False:
        right+=1


print(left,right)    