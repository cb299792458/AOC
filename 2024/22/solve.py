from collections import deque, defaultdict

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

# # part 1
# total = 0
# for num in nums:
#     for _ in range(2000):
#         num = process(num)
#     total += num
# print(total)

# part 2
totals = defaultdict(int)
for num in nums:
    prev = num
    last_four = deque()
    seen = set()

    for _ in range(2000):
        num = process(num)
        last_price = prev % 10
        price = num % 10
        last_four.append(price - last_price)
        if len(last_four) > 4:
            last_four.popleft()
        
        if len(last_four) == 4:
            key = tuple(last_four)
            # if key == (-2,1,-1,3):
            #     print(price)
            if key not in seen:
                seen.add(key)
                totals[key] += price
        
        prev = num

everything = list(totals.items())
everything.sort(key=lambda x: x[1])
print(everything[-1])
