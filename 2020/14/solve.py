input = [l[:-1] for l in open('input.txt','r').readlines()]
BITS = 36


def dec(chars):
    val = 0
    for char in chars:
        val *= 2
        val += int(char)
    return val

def dec_to_bin(num):
    return str(bin(num)[2:])

# # part 1
# def digit(mask, val, i):
#     if mask[i] != 'X':
#         return mask[i]
#     if i + len(val) >= BITS:
#         return val[i - BITS + len(val)]
#     return '0'

# memory = dict()
# for line in input:
#     if line[:4] == 'mask':
#         mask = line.split()[2]
#         # print(mask)
#     elif line[:3] == 'mem':
#         [index, _, val] = line.split()
#         index = int(index[4:-1])

#         val = int(val)
#         val = dec_to_bin(val)
#         memory[index] = [digit(mask, val, i) for i in range(BITS)]

#     else:
#         raise 'unexpected line'

# total = 0
# for chars in memory.values():
#     total += dec(chars)
# print(total)

# part 2

def apply_mask(mask, index):
    chars = list(dec_to_bin(index))
    chars = ['0'] * (BITS - len(chars)) + chars
    for [i, char] in enumerate(mask):
        if char != '0':
            chars[i] = char
    return chars

memory = dict()
for line in input:
    if line[:4] == 'mask':
        mask = line.split()[2]
    elif line[:3] == 'mem':
        [index, _, val] = line.split()
        index = int(index[4:-1])

        val = int(val)

        index = apply_mask(mask, index)
        indices = [0]

        for char in index:
            new_indices = []
            for prev in indices:
                if char != '1':
                    new_indices.append(prev * 2)
                if char != '0':
                    new_indices.append(prev * 2 + 1)

            indices = new_indices
        for i in indices:
            memory[i] = val

print(sum(int(v) for v in memory.values()))