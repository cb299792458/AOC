input = [l[:-1] for l in open('input.txt','r').readlines()]

p1 = 4
p2 = 8
# s1 = 0
# s2 = 0
# die = 0
# rolls = 0

# while s1<1000 and s2<1000:
#     for _ in range(3):
#         die += 1
#         p1 += die
#         while p1>10:
#             p1 -= 10
#         rolls += 1
#         if die>=100: die = 0
#     s1 += p1
#     if s1 >= 1000:
#         print(s1,s2,rolls)


#     for _ in range(3):
#         die += 1
#         p2 += die
#         while p2>10:
#             p2 -= 10
#         rolls += 1
#         if die>=100: die  = 0
#     s2 += p2
#     if s2>= 1000:
#         print(s1,s2,rolls)

from collections import Counter, deque
perms = Counter()
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            perms[i+j+k] += 1

win1 = 0
win2 = 0

start = (0,  0,  p1, p2, True,    1)
#        s1, s2, p1, p2, p1_turn, universes
queue = deque([start])
while queue:
    (s1, s2, p1, p2, p1_turn, universes) = queue.popleft()
    if s1 >= 21:
        win1 += universes
        continue
    if s2 >= 21:
        win2 += universes
        continue

    for [die, branches] in perms.items():
        if p1_turn:
            new_p1 = p1 + die
            if new_p1 > 10: new_p1 -= 10
            new_s1 = s1 + new_p1
            queue.append((new_s1, s2, new_p1, p2, False, universes*branches))
        else:
            new_p2 = p2 + die
            if new_p2 > 10: new_p2 -= 10
            new_s2 = s2 + new_p2
            queue.append((s1, new_s2, p1, new_p2, True, universes*branches))

print(win1, win2)
