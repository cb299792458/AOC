input = [l[:-1] for l in open('input.txt','r').readlines()]
a = int(input[0].split(' ')[-1])
b = int(input[1].split(' ')[-1])
c = int(input[2].split(' ')[-1])

program = [int(n) for n in input[-1].split(' ')[1].split(',')]

def combo(n):
    if n<4:
        return n
    if n==4:
        return a
    if n==5:
        return b
    if n==6:
        return c
    raise Exception('Invalid combo', n)

print(a,b,c,program)
output = []
i = 0
while i < len(program):
    [opcode, operand] = program[i:i+2]
    match opcode:
        case 0:
            a = a // (2**combo(operand))
        case 1:
            b = b ^ operand
        case 2:
            b = combo(operand) % 8
        case 3:
            if a:
                i = operand
                continue
        case 4:
            b = b ^ c
        case 5:
            output.append(combo(operand) % 8)
        case 6:
            b = a // (2**combo(operand))
        case 7:
            c = a // (2**combo(operand))

    i += 2

print(','.join([str(n) for n in output]))
