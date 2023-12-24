input = [l[:-1] for l in open('input.txt','r').readlines()]
hailstones = []
for line in input:
    pos, vel = line.split(' @ ')
    px,py,pz = map(int,pos.split(', '))
    vx,vy,vz = map(int,vel.split(', '))
    hailstones.append((px,py,pz,vx,vy,vz))

# collisions = 0
# test = (200000000000000,400000000000000)
# for i in range(len(hailstones)):
#     for j in range(i+1,len(hailstones)):
#         pxa,pya,_,vxa,vya,_ = hailstones[i]
#         pxb,pyb,_,vxb,vyb,_ = hailstones[j]
#         ma, mb = vya/vxa, vyb/vxb
#         if ma==mb: continue

#         x = ((-mb*pxb)+pyb+(ma*pxa)-pya)/(ma-mb)
#         if x<test[0] or x>test[1]: continue

#         y = ma*(x-pxa)+pya
#         if y<test[0] or y>test[1]: continue

#         if x>pxa and vxa<0: continue
#         if x<pxa and vxa>0: continue
#         if x>pxb and vxb<0: continue
#         if x<pxb and vxb>0: continue
        
#         collisions += 1
# print(collisions)


for hailstone in hailstones[5:9]:
    px,py,pz,vx,vy,vz = hailstone
    print(f'(x-{px})/({vx}-a)=(y-{py})/({vy}-b)=(z-{pz})/({vz}-c)')

print(200_027_938_836_082+127_127_087_242_193+219_339_468_239_370)