input = [l[:-1] for l in open('input.txt','r').readlines()]
all_nums = [line.split(':')[1] for line in input]

# part 1
total = 0
for line in all_nums:
    [winners, ticket] = line.split('|')
    winners = [num for num in winners.split(' ') if num]
    ticket = [num for num in ticket.split(' ') if num]
    
    points = 0
    for t in ticket:
        if t in winners:
            points = (points*2) or 1
    
    total += points

print(total)

# part 2
cards = [1] * len(all_nums)
for i, line in enumerate(all_nums):
    [winners, ticket] = line.split('|')
    winners = [num for num in winners.split(' ') if num]
    ticket = [num for num in ticket.split(' ') if num]

    matches = 0
    for t in ticket:
        if t in winners:
            matches += 1
    
    for card_inc in range(1,matches+1):
        idx = i + card_inc
        if idx < len(all_nums):
            cards[idx] += cards[i]

print(sum(cards))