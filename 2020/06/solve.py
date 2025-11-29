with open('input.txt', 'r') as f:
    blocks = f.read().strip().split("\n\n")

alphabet = 'qwertyuiopasdfghjklzxcvbnm'
chars = [c for c in alphabet]

count = 0
for block in blocks:
    lines = block.split('\n')
    count += len([c for c in chars if all([c in line for line in lines])])
print(count)
