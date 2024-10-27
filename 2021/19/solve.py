from collections import defaultdict, deque
input = [l[:-1] for l in open('input.txt','r').readlines()]

def get_rotations(orig):
    [x,y,z] = orig
    return [
        (x, y, z),
        (x, -z, y),
        (x, -y, -z),
        (x, z, -y),
        (-x, -y, z),
        (-x, z, y),
        (-x, y, -z),
        (-x, -z, -y),
        (y, z, x),
        (y, -x, z),
        (y, -z, -x),
        (y, x, -z),
        (-y, -z, x),
        (-y, x, z),
        (-y, z, -x),
        (-y, -x, -z),
        (z, x, y),
        (z, -y, x),
        (z, -x, -y),
        (z, y, -x),
        (-z, -x, y),
        (-z, y, x),
        (-z, x, -y),
        (-z, -y, -x)
    ]


def overlaps(list1, list2):
    return set(list1).intersection(set(list2))

def manhattan(v,w):
    return abs(v[0]-w[0])+abs(v[1]-w[1])+abs(v[2]-w[2])

def get_vectors(beacons):
    vectors = []
    for i in range(len(beacons)):
        for j in range(len(beacons)):
            if i != j:
                vectors.append((beacons[i][0]-beacons[j][0],beacons[i][1]-beacons[j][1],beacons[i][2]-beacons[j][2]))
    return vectors

# {scanner_idx: beacon_array}
scanners = defaultdict(list)
scanner_idx = -1
for line in input:
    if not line:
        continue
    if 'scanner' in line:
        scanner_idx += 1
    else:
        scanners[scanner_idx].append(tuple(map(int,line.split(','))))

# {scanner_idx: vector_array}
vectors = dict()
for [i, beacons] in scanners.items():
    vectors[i] = get_vectors(beacons)

#{scanner_idx: {rotation_idx: rotated_difference_array}}
all_rotations = defaultdict(lambda: defaultdict(list))
for [scanner_idx, vectors] in vectors.items():
    for vector in vectors:
        for i, rotation in enumerate(get_rotations(vector)):
            all_rotations[scanner_idx][i].append(rotation)

all_beacons = set()
seen = set()
def add_beacons(offX,offY,offZ,rotI,scannerI):
    duplicates = 0
    for [x,y,z] in scanners[scannerI]:
        [x,y,z] = get_rotations([x,y,z])[rotI]
        beacon = (x+offX,y+offY,z+offZ)
        if beacon in all_beacons:
            duplicates += 1
        all_beacons.add((x+offX,y+offY,z+offZ))
    print(f"Added beacons from scanner {scannerI}, there were {duplicates} duplicates")

# q = [(0,0,0,0,0)]
# while q:
#     [offX,offY,offZ,rotI,scannerI] = q.pop(0)
#     add_beacons(offX,offY,offZ,rotI,scannerI)
#     seen.add(scannerI)
#     prev_differences = get_vectors(all_beacons)

#     for scanner_idx in scanners:
#         if scanner_idx in seen:
#             continue
#         rot_i = -1
#         for [i, differences] in all_rotations[scanner_idx].items():
#             curr_overlaps = overlaps(prev_differences, differences)
#             if len(curr_overlaps) >= 132:
#                 rot_i = i
#                 break
#         if rot_i == -1:
#             continue
        
#         rotated_points = all_rotations[scanner_idx][rot_i]
#         for x_off in range(-1000,1001):
#             for y_off in range(-1000,1001):
#                 for z_off in range(-1000,1001):
#                     curr_overlaps = 0
#                     for rotated_point in rotated_points:
#                         [x,y,z] = rotated_point
#                         if (x+x_off,y+y_off,z+z_off) in all_beacons:
#                             curr_overlaps += 1
#                     if curr_overlaps >= 1:
#                         print(curr_overlaps)

def get_rotation_index(scanner_idx):
    if not scannerI:
        return 0
    
    most_overlaps = 0
    res = -1
    prev_vectors = get_vectors(list(all_beacons))
    for i in range(24):
        curr_overlaps = len(overlaps(prev_vectors, all_rotations[scanner_idx][i]))
        if curr_overlaps > most_overlaps:
            most_overlaps = curr_overlaps
            res = i
    if most_overlaps < 132:
        print(f"Scanner {scanner_idx} has no valid rotation")
    return res

def get_offset(scanner_idx, rot_idx):
    if not scannerI:
        return (0,0,0)
    res = [0,0,0]
    rotated_points = [get_rotations(beacon)[rot_idx] for beacon in scanners[scanner_idx]]
    all_beacon_list = list(all_beacons)

    for k in range(3):
        most_overlaps = 0
        possible_offsets = []
        for rotated_point in rotated_points:
            for beacon in all_beacon_list:
                possible_offsets.append(beacon[k] - rotated_point[k])

        for offset in possible_offsets:
            curr_overlaps = 0
            for rotated_point in rotated_points:
                for beacon in all_beacon_list:
                    if rotated_point[k] + offset == beacon[k]:
                        curr_overlaps += 1
            if curr_overlaps > most_overlaps and curr_overlaps >= 12:
                most_overlaps = curr_overlaps
                res[k] = offset
                # print(f"Most overlaps for {k} is {most_overlaps}")
    # print(res)
    return res

# made an adj list for overlapping beacons
adjacencies = defaultdict(list)
for s1 in range(len(scanners)):
    for s2 in range(len(scanners)):
        if s1 == s2:
            continue
        for i in range(48):
            rotated = all_rotations[s2][i]
            ols = overlaps(all_rotations[s1][0], rotated)
            if len(ols) >= 132:
                adjacencies[s1].append(s2)
                break
# print(adjacencies)

all_scanners = []

q = deque([0])
while q:
    scannerI = q.popleft()
    if scannerI in seen:
        continue

    rotI = get_rotation_index(scannerI)
    (offX,offY,offZ) = get_offset(scannerI, rotI)
    all_scanners.append((offX,offY,offZ))
    # print(f"Scanner {scannerI} has rotation {rotI} and offset {offX},{offY},{offZ}")

    add_beacons(offX,offY,offZ,rotI,scannerI)
    seen.add(scannerI)

    for adj in adjacencies[scannerI]:
        q.append(adj)


max_dist = 0
for s1 in all_scanners:
    for s2 in all_scanners:
        max_dist = max(max_dist, manhattan(s1,s2))
print(max_dist)
