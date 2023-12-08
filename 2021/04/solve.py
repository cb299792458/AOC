input = [l[:-1] for l in open('input.txt','r').readlines()]
nums = input[0].split(',')

all_rows = input[2:]

class Card():
    def __init__(self,rows):
        self.nums = set()
        self.rows = [set() for _ in range(5)]
        self.cols = [set() for _ in range(5)]
        self.won = False

        for r,row in enumerate(rows):
            row = row.split()
            for c, num in enumerate(row):
                self.nums.add(num)
                self.rows[r].add(num)
                self.cols[c].add(num)

    def win(self,num):
        self.won = True
        print(sum([int(n) for n in self.nums])*int(num))

    def mark(self,num):
        if self.won: return
        self.nums.discard(num)
        for row in self.rows:
            row.discard(num)
            if not len(row):
                self.win(num)
        for col in self.cols:
            col.discard(num)
            if not len(col):
                self.win(num)


cards = []
for i in range(0,len(all_rows), 6):
    cards.append(Card(all_rows[i:i+5]))

for num in nums:
    for card in cards:
        card.mark(num)
