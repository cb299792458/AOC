rounds = open('input.txt','r').readlines()

you = ['X','Y','Z']
opp = ['A','B','C']

score=0
for round in rounds:
    # # part 1
    # score += 1
    # score += you.index(round[2])

    # if you.index(round[2])==opp.index(round[0]): score += 3
    # if you.index(round[2])==(opp.index(round[0])+1)%3: score += 6

    # part 2
    score += 3*you.index(round[2])
    index_offset = you.index(round[2]) - 1
    your_play = you[(opp.index(round[0])+index_offset)%3]
    score += you.index(your_play) + 1


print(score)