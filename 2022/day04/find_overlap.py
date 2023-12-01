assignments=open('input.txt','r').readlines()
assignments=[a[:-1] for a in assignments]
formatted=[]

for a in assignments:
    [a1,a2]=a.split(',')
    [s1,e1]=a1.split('-')
    [s2,e2]=a2.split('-')
    res = [int(x) for x in [s1,e1,s2,e2]]
    formatted.append(res)

# print(formatted)

pairs=0

for [s1,e1,s2,e2] in formatted:
    # if (s1<=s2 and e1>=e2) or (s1>=s2 and e1<=e2): pairs+=1
    if (s1<=e2 and e1>=s2) or (s2<=e1 and e2>=s1): pairs+=1

print(pairs)