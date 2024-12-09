input = [l[:-1] for l in open('input.txt','r').readlines()]

input = input[0]

id = 0
stack = []

# # part 1
# file = True
# for c in input:
#     if file:
#         for _ in range(int(c)):
#             stack.append(id)
#         id += 1
#         file = False
#     else:
#         for _ in range(int(c)):
#             stack.append('.')
#         file = True

# empty_index = 0
# while stack[empty_index] != '.':
#     empty_index += 1

# while empty_index < len(stack):
#     last = stack.pop()
#     if last == '.':
#         continue
#     stack[empty_index] = last

#     while empty_index < len(stack) and stack[empty_index] != '.':
#         empty_index += 1

# checksum = 0
# for i,n in enumerate(stack):
#     checksum += i*n
# print(checksum)

# part 2
file = "FILE"
empty = "EMPTY"
for [i, c] in enumerate(input):
    if i%2:
        stack.append((empty, int(c), None))
    else:
        stack.append((file, int(c), id))
        id += 1

stack_copy = stack.copy()
while stack_copy:
    (data, size, id) = stack_copy.pop()
    if data == empty:
        continue

    new_idx = -1
    for [i, (data2, size2, id2)] in enumerate(stack):
        if data2 == empty and size2 >= size:
            new_idx = i
            break
        if id == id2:
            break
    
    if new_idx != -1:
        (_, size3, _) = stack[new_idx]
        stack[new_idx] = (file, size, id)

        if size3 > size:
            stack.insert(new_idx+1, (empty, size3-size, None))

        delete_idx = len(stack)-1
        while stack[delete_idx][2] != id:
            delete_idx -= 1
        stack[delete_idx] = (empty, size, None)

fragmented = []
for (_, size, id) in stack:
    for _ in range(size):
        fragmented.append(id)

checksum = 0
for [i, n] in enumerate(fragmented):
    if n:
        checksum += i*n
print(checksum)
