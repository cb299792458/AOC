from collections import Counter
input = [l[:-1] for l in open('input.txt','r').readlines()]

data = [(d.split()[0], int(d.split()[1])) for d in input]

# part 1
ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
def rank(c):
    return ranks[c] if c in ranks else int(c)

def sort_hand(tup):
    (hand, _) = tup
    counts = sorted(Counter(hand).values(), reverse=True)
    counts += [0,0]
    hand_type = counts[0] + (0.5 if counts[1]==2 else 0)

    return [hand_type] + [rank(c) for c in hand]

data.sort(key=sort_hand)

winnings = 0
for i,(_,bid) in enumerate(data):
    winnings += (i+1)*bid
print(winnings)

# part 2
ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}

def sort_hand(tup):
    (hand, _) = tup
    counts = Counter(hand)
    jokers = counts.pop('J',0)
    counts = list(counts.values())
    counts.sort(reverse=True)
    counts += [0,0]
    counts[0] += jokers

    hand_type = counts[0] + (0.5 if counts[1]==2 else 0)

    return [hand_type] + [rank(c) for c in hand]

data.sort(key=sort_hand)

winnings = 0
for i,(_,bid) in enumerate(data):
    winnings += (i+1)*bid
print(winnings)