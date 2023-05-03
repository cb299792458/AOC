input=open('input.txt','r').readlines()
input=[a[:-1] for a in input]

# print(input[0])
s = input[0]

i=14
while True:
    if len(set([*s[i-14:i]]))==14:
        print(i)
        break
    i+=1

