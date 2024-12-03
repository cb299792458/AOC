input = [l[:-1] for l in open('input.txt','r').readlines()]
input = ''.join(input)

res = 0
enabled = True

def process(s):
    n1, n2 = s.split(',')
    n1 = int(n1)
    n2 = int(n2)
    global res
    res += n1*n2

i = 4
while i < len(input):
    if input[i-4:i] == 'mul(':
        j=i
        valid = True
        while input[i] != ')':
            if input[i] not in '(1234567890),':
                valid = False
                break
            i += 1
        if valid and enabled:
            process(input[j:i])

    if input[i-4:i] == 'do()':
        enabled = True
    if input[i-7:i] == "don't()":
        enabled = False

    i+=1

print(res)
