input = [l[:-1] for l in open('input.txt','r').readlines()]

algo = ''.join(input[:1])
orig = input[2:]
extra = 150
R = len(orig) + 2*extra
C = len(orig[0]) + 2*extra

image = [['.' for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if extra<=r<R-extra:
            if extra<=c<C-extra:
                if orig[r-extra][c-extra]=='#':
                    image[r][c]='#'


def enhance(image):
    new = [['.' for _ in range(C)] for _ in range(R)]
    for r in range(1,R-1):
        for c in range(1,C-1):
            pixel = ''.join([''.join(image[nr][c-1:c+2]) for nr in range(r-1,r+2)])

            idx = 0
            for char in pixel:
                idx*=2
                if char=='#':
                    idx+=1
            new[r][c] = algo[idx]
    
    return new

for _ in range(25):
    image = enhance(image)
    image = enhance(image)

for line in image:
    print(''.join(line))

lit = 0
for r in range(50,R-50):
    for c in range(2,C):
        if image[r][c]=='#':
            lit += 1
print(lit)
