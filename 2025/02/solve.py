input = [l[:-1] for l in open('input.txt','r').readlines()]
input = input[0]

def is_invalid(num):
    s = str(num)
    N = len(s)
    if N % 2:
        return False
    return s[:N//2] == s[N//2:]

def factors(num):
    res = []
    for n in range(2, num + 1):
        if not num % n:
            res.append(n)
    return res

def parts(string, parts):
    size = len(string) // parts
    res = []
    for i in range(0, len(string), size):
        res.append(string[i:i+size])
    return res

def is_invalid2(num):
    s = str(num)
    for f in factors(len(s)):
        p = parts(s, f)
        if all([part == p[0] for part in p]):
            return True
    return False


total = 0

for num_range in input.split(','):
    [start, final] = num_range.split('-')
    for num in range(int(start), int(final) + 1):
        if is_invalid2(num):
            # print(num)
            total += num

print(total)

