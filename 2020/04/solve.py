with open('input.txt', 'r') as f:
    blocks = f.read().strip().split("\n\n")

required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

valid = 0

def is_valid(d):
    if not all(k in passport for k in required):
        return False
    
    byr = d['byr']
    if len(byr) != 4:
        return False
    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return False
    
    iyr = d['iyr']
    if len(iyr) != 4:
        return False
    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = d['eyr']
    if len(eyr) != 4:
        return False
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False
    
    hgt = d['hgt']
    if hgt[-2:] == 'in':
        hgt = int(hgt[:-2])
        if hgt < 59 or hgt > 76:
            return False
    elif hgt[-2:] == 'cm':
        hgt = int(hgt[:-2])
        if hgt < 150 or hgt > 193:
            return False
    else:
        return False

    hcl = d['hcl']
    if hcl[0] != '#':
        return False
    if not all(c in '0123456789abcdef' for c in hcl[1:]):
        return False
    
    ecl = d['ecl']
    if ecl not in [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    ]:
        return False

    if len(d['pid']) != 9:
        return False

    return True
    
    
for block in blocks:
    passport = dict()
    pairs = block.split()
    for pair in pairs:
        [k, v] = pair.split(':')
        passport[k] = v
    
    if is_valid(passport):
        valid += 1
print(valid)
