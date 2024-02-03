input = [l[:-1] for l in open('input.txt','r').readlines()]

def explode(s):
    stack = []
    most_pairs = pairs = 0
    for c in s:
        if c.isnumeric():
            if stack[-1].isnumeric():
                stack[-1] += c
            else:
                stack.append(c)
        else:
            if c=='[':
                pairs += 1
                most_pairs = max(most_pairs, pairs)
            elif c==']':
                pairs -= 1
            else:
                pass
            stack.append(c)
    if most_pairs<5: return s

    exploded = False
    i = 0
    while i < len(stack):
        c = stack[i]
        if c=='[':
            if pairs==4 and not exploded:
                exploded = True
                inside = ''
                stack.pop(i)
                while stack[i] != ']':
                    inside += stack.pop(i)
                stack.pop(i)

                [l,r] = map(int,inside.split(','))

                j = i
                while j>-1 and not stack[j].isnumeric():
                    j -= 1
                if j!=-1:
                    stack[j] = str(int(stack[j]) + int(l))

                k = i
                while k<len(stack) and not stack[k].isnumeric():
                    k += 1
                if k!=len(stack):
                    stack[k] = str(int(stack[k]) + int(r))

                stack.insert(i,'0')
            else:
                pairs += 1
        elif c==']':
            pairs -= 1
        i += 1
    return ''.join(stack)

def split(s):
    stack = []
    for c in s:
        if c.isnumeric():
            if stack[-1].isnumeric():
                stack[-1] += c
            else:
                stack.append(c)
        else:
            stack.append(c)

    splitted = False
    for i,c in enumerate(stack):
        if not splitted and c.isnumeric() and int(c)>9:
            splitted = True
            c = int(c)
            stack[i] =f'[{c//2},{(c+1)//2}]' 
    return ''.join(stack)
    

def add(s1,s2):
    res = f'[{s1},{s2}]'

    while True:
        new = explode(res)
        if new != res:
            res = new
            continue

        new = split(res)
        if new != res:
            res = new
            continue

        break

    return res

def magnitude(s):
    stack = []
    for c in s:
        if c==',': continue
        if c=='[': stack.append(c)
        if c.isnumeric():
            stack.append(int(c))
        if c==']':
            r = stack.pop()
            l = stack.pop()
            stack.pop()
            stack.append(3*l + 2*r)

    # print(stack)
    return stack[0]

# # part 1
# total = input[0]
# for line in input[1:]:
#     total = add(total, line)
# # print(total)
# magnitude(total)

# part 2
best = 0
for line1 in input:
    for line2 in input:
        best = max(best, magnitude(add(line1,line2)))
print(best)
