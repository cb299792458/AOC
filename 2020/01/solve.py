input = [l[:-1] for l in open('input.txt','r').readlines()]

seen = set()
for line in input:
    num = int(line)
    if 2020 - num in seen:
        print((2020-num) * num)
    seen.add(num)

M = len(input)
for i in range(M):
    for j in range(i+1, M):
        for k in range(j + 1, M):
            n1, n2, n3 = int(input[i]), int(input[j]), int(input[k])
            if n1 + n2 + n3 == 2020:
                print(n1*n2*n3)
