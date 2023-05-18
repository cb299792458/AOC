input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

hashmap = dict()
for line in input:
    words = line.split()
    key = words[0][:-1]

    if len(words)==2: hashmap[key] = int(words[1])
    else:
        hashmap[key] = words[1:]

# print(hashmap)
original=hashmap.copy()
fns = {
    '+': lambda x,y: x+y,
    '-' :lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
}

path_from_humn = ['humn']

while type(hashmap['root']) != int:
    for key in hashmap:
        if type(hashmap[key])==int: continue

        [mon1,operand,mon2] = hashmap[key]
        if type(hashmap[mon1])!=int or type(hashmap[mon2])!=int: continue

        hashmap[key] = int( fns[operand](hashmap[mon1],hashmap[mon2]) )
        # if key=='root': print(f'root is comparing {hashmap[mon1]} and {hashmap[mon2]}')
        if mon1==path_from_humn[-1] or mon2==path_from_humn[-1]:
            path_from_humn.append(key)

print(hashmap['root'])



path_from_humn.reverse()
# print(path_from_humn)

# Root should get the number 22931068684876 twice

updated = dict()
updated['root'] = 22931068684876
updated['tlpd'] = 22931068684876
updated['humn'] = '?'

for i in range(2,len(path_from_humn)): #range(len(path_from_humn)-1):
    answer = updated[path_from_humn[i-1]]
    term1 = path_from_humn[i]
    # print(answer,term1)

    [s1,op,s2] = original[path_from_humn[i-1]]
    # print(s1,op,s2)

    other = hashmap[s1] if s1!= term1 else hashmap[s2]
    # print(other)

    if op=='/':
        if s1==term1:
            updated[term1] = answer * other
        else:
            updated[term1] = other / answer
    if op=='*':
        updated[term1] = answer / other
    if op=='+':
        updated[term1] = answer - other
    if op=='-':
        if s1==term1:
            updated[term1] = answer + other
        else:
            updated[term1] = other - answer
    # print('DONE')

print(updated['humn']) # change humn to this and run again