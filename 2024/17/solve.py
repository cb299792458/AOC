input = [l[:-1] for l in open('input.txt','r').readlines()]
original_a = int(input[0].split(' ')[-1])
a = original_a
b = int(input[1].split(' ')[-1])
c = int(input[2].split(' ')[-1])

program = [int(n) for n in input[-1].split(' ')[1].split(',')]

# # part 1
# def combo(n):
#     if n<4:
#         return n
#     if n==4:
#         return a
#     if n==5:
#         return b
#     if n==6:
#         return c

# print(a,b,c,program)
# output = []
# i = 0
# while i < len(program):
#     [opcode, operand] = program[i:i+2]
#     match opcode:
#         case 0:
#             a = a // (2**combo(operand))
#         case 1:
#             b = b ^ operand
#         case 2:
#             b = combo(operand) % 8
#         case 3:
#             if a:
#                 i = operand
#                 continue
#         case 4:
#             b = b ^ c
#         case 5:
#             output.append(combo(operand) % 8)
#         case 6:
#             b = a // (2**combo(operand))
#         case 7:
#             c = a // (2**combo(operand))

#     i += 2

# print('[' + ', '.join([str(n) for n in output])+ ']')

"""   octal number  0        0
Program    A        B        C
  2 4               =A%8                          get last digit
  1 3               =(A%8)^3                      xor last digit with 3 
  7 5                        =A//(2**((A%8)^3))   set c to a right shifted by b
  0 3      =A//8                                  pop last digit
  1 5               =0                            set b to 0 (b^b is always 0)
  4 1               =A//(2**((A%8)^3))            set b to c (0^c is always c)
  5 5               output b%8                    output b (aka c) % 8
  3 0                                             restart if a!=0 (until a is 0)
"""

# part 2

def run(decimal):
    a = decimal
    b = 0
    c = 0
    output = []

    while a:
        b = a % 8
        b = b ^ 3
        c = a >> b
        a = a // 8
        b = b ^ 5 ^ c
        output.append(b % 8)

    return output

answers = []

def backtrack(curr_num, curr_i):
    if curr_i == -1:
        answers.append(curr_num)
        return

    for n in range(8):
        adend = n * (8**curr_i)
        output = run(curr_num + adend)

        if len(output) > curr_i and output[curr_i] == program[curr_i]:
            backtrack(curr_num + adend, curr_i-1)

backtrack(0,15)
print(answers)
print()
print(program)
print(run(answers[0]))
