from collections import defaultdict
input = [l[:-1] for l in open('input.txt','r').readlines()]
first_space = input.index('')

fields = input[:first_space]

your_ticket = input[first_space + 2]
your_ticket = [int(n) for n in your_ticket.split(',')]

nearby_tickets = input[first_space + 5:]
nearby_tickets = [[int(n) for n in line.split(',')] for line in nearby_tickets]

# print(fields)
# print(your_ticket)
# print(nearby_tickets)

all_ranges = []
fields_by_name = defaultdict(list)

for line in fields:
    [name, nums] = line.split(': ')
    ranges = nums.split(' or ')
    for r in ranges:
        [small, large] = r.split('-')
        all_ranges.append((int(small), int(large)))
        fields_by_name[name].append((int(small), int(large)))

def is_valid(num):
    for (small, large) in all_ranges:
        if small <= num <= large:
            return True
    return False
# # part 1

# error_rate = 0

# for row in nearby_tickets:
#     for num in row:
#         if not is_valid(num):
#             print(num)
#             error_rate += num

# print(error_rate)

# part 2
def is_valid_row(row):
    for num in row:
        if not is_valid(num):
            return False
    return True

valid_rows = []
for row in nearby_tickets:
    if is_valid_row(row):
        valid_rows.append(row)

nums_by_index = defaultdict(list)
for row in valid_rows:
    for [i, num] in enumerate(row):
        nums_by_index[i].append(num)

def is_valid_for_field(num, field):
    ranges = fields_by_name[field]
    for [small, large] in ranges:
        if small <= num <= large:
            return True
    return False

def nums_could_match_field(nums, field):
    for num in nums:
        if not is_valid_for_field(num, field):
            return False
    return True

identified = dict()
used_indices = set()
while len(identified) < len(fields):
    possible_indices_for_field = defaultdict(list)
    for [i, nums] in nums_by_index.items():
        if i in used_indices:
            continue
        for field in fields_by_name.keys():
            if field in identified:
                continue
            if nums_could_match_field(nums, field):
                possible_indices_for_field[field].append(i)
    for [field, possible_indices] in possible_indices_for_field.items():
        if len(possible_indices) == 1:
            index = possible_indices[0]
            identified[field] = index
            used_indices.add(index)
            break

KEYWORD = 'departure'
ans = 1
for [name, index] in identified.items():
    if name[:len(KEYWORD)] == KEYWORD:
        ans *= your_ticket[index]

print(ans)