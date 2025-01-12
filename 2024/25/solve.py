input = open('input.txt','r').read().strip()
grids = [line.split('\n') for line in input.split('\n\n')]

locks = []
keys = []

for grid in grids:
    if grid[0] == '#####':
        lock = [0] * 5
        for r in range(7):
            for c in range(5):
                if grid[r][c] == '#':
                    lock[c] = r
        locks.append(lock)

    elif grid[0] == '.....':
        key = [0] * 5
        for r in range(6,-1,-1):
            for c in range(5):
                if grid[r][c] == '#':
                    key[c] = 6-r
        keys.append(key)
    else:
        print('uh oh')

# print(locks, keys)
def fits(lock, key):
    for i,(k, l) in enumerate(zip(key, lock)):
        if k+l >= 6:
            return False
    return True

ans = 0
for lock in locks:
    for key in keys:
        if fits(lock, key):
            ans += 1
print(ans)
