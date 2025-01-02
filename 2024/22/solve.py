input = [l[:-1] for l in open('input.txt','r').readlines()]

nums = [int(line) for line in input]

def mix(value, secret):
    return value ^ secret
def prune(secret):
    return secret % 16777216

def process(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret//32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

total = 0
for num in nums:
    for _ in range(2000):
        num = process(num)
    total += num
print(total)
