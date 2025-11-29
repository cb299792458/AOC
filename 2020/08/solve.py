input = [l[:-1] for l in open('input.txt','r').readlines()]
# seen = set()
# acc = 0

# index = 0
# while index not in seen:
#     seen.add(index)
#     instructions = input[index]
#     [op, arg] = instructions.split()
#     num = int(arg)
#     match op:
#         case 'acc':
#             acc += num
#             index += 1
#         case 'jmp':
#             index += num
#         case 'nop':
#             index += 1

# print(acc)

def skip(i):
    seen = set()
    acc = 0
    index = 0

    while index not in seen:
        if index >= len(input):
            print(acc)
            break
        seen.add(index)

        instructions = input[index]
        [op, arg] = instructions.split()
        num = int(arg)

        match op:
            case 'acc':
                acc += num
                index += 1
            case 'jmp':
                index += num if index != i else 1
            case 'nop':
                index += 1 if index != i else num

for i in range(len(input)):
    skip(i)
