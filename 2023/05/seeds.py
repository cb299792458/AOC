input = [l[:-1] for l in open('input.txt','r').readlines()]

blocks = []
curr = []
for line in input+['']:
  if line == '':
    blocks.append(curr)
    curr = []
  else:
    curr.append(line)

seeds = []
for word in blocks[0][0].split()[1:]:
  seeds.append(int(word))

maps = dict()
for block in blocks[1:]:
  name = block[0].split()[0]
  temp = []
  for line in block[1:]:
    dest, source, length = map(int,line.split())
    temp.append([dest,source,length])
  maps[name] = temp

def convert(prevs, key):
  conversions = maps[key]
  res = []
  for prev in prevs:
    added = False
    for [dest, source, length] in conversions:
      if source <= prev < source+length:
        res.append(dest + prev - source)
        added = True
        break # no overlap -> unnecessary
    if not added: res.append(prev)
  return res

keys = list(maps.keys())

# part 1
data = seeds
for key in keys:
  data = convert(data,key)
# print(data)
# print(min(data))

# part 2
seed_ranges = []
for i in range(len(seeds)//2):
  seed_ranges.append((seeds[2*i], seeds[2*i]+seeds[2*i+1]-1))
seed_ranges.sort()

def convert_ranges(ranges, key):
  conversions = maps[key]
  res = []
  for start, end in ranges:
    unconverted = [start,end]

    for [dest, source_start, length] in conversions:

      source_end = source_start + length - 1
      diff = dest - source_start
      
      if end < source_start or start > source_end: # no conversion
        continue
      if start >= source_start and end <= source_end: # full conversion
        res.append((start + diff, end + diff))
        unconverted=[float('inf'), -float('inf')]
        continue

      if start<=source_start and not end>=source_end:
        res.append((source_start + diff, end + diff))
        unconverted[1] = min(unconverted[1], source_start-1)

      elif start<=source_start and end>=source_end:
        res.append((source_start + diff, source_end + diff))
        unconverted[1] = min(unconverted[1], source_start-1)
        unconverted[0] = max(unconverted[0], source_end+1)

      elif not start<=source_start and end>=source_end:
        res.append((start + diff, source_end + diff))
        unconverted[0] = max(unconverted[0], source_end+1)

      else:
        print('miss')

    if unconverted[0]<=unconverted[1]:
      # print('didnt convert', unconverted)
      res.append((unconverted[0],unconverted[1]))
    
  # print(res)
  return res

range_data = seed_ranges
for key in keys:
  range_data = convert_ranges(range_data,key)
range_data.sort()
print(range_data)