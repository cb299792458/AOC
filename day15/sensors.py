input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]
from collections import defaultdict

coords=[]
for line in input:
    words = line.split()
    sx = int(words[2][2:-1])
    sy = int(words[3][2:-1])

    bx = int(words[-2][2:-1])
    by = int(words[-1][2:])
    coords.append((sx,sy,bx,by))

# no_beacon = set()
# for sx,sy,bx,by in coords:
#     dist = abs(sx-bx) + abs(sy-by)
#     sideways = dist-abs(2000000-sy)
#     # print(sideways)
#     for i in range(sx-sideways,sx+sideways+1):
#         no_beacon.add(i)

# # remove actual beacon spots
# for sx,sy,bx,by in coords:
#     if by==2000000: no_beacon.discard(bx)

# print(len(no_beacon))
# # print(no_beacon)
def check(x,y):
    for sx,sy,bx,by in coords:
        dist = abs(sx-bx) + abs(sy-by)
        if abs(sx-x) + abs(sy-y) <= dist: return False
    return True

to_check = defaultdict(int)
most=0
def add_point(x,y):
    global most
    if x<0 or y<0 or x>4000000 or y>4000000: return
    # to_check[x,y]+=1
    # if to_check[x,y]>most:
    #     print(x,y)
    #     most=to_check[x,y]
    # most+=1
    if check(x,y): print(x,y)
# for sx,sy,bx,by in coords:
#     dist = abs(sx-bx) + abs(sy-by) + 1

#     diff=0
#     # add all points just outside the diamond
#     # go diagonally from each vertex
#     while diff < dist:
#         add_point(sx+dist-diff,sy+diff)
#         add_point(sx-dist+diff,sy-diff)
#         add_point(sx-diff,sy+dist-diff)
#         add_point(sx+diff,sy-dist+diff)
#         diff+=1

# print(to_check)
# print(len(to_check))



print(most)

print(2706598*4000000+3253551)