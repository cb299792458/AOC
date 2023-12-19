import sys
inf = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

ll = [x for x in open(inf).read().strip().split('\n')]
parse = {'0':'0000',
'1':'0001',
'2':'0010',
'3':'0011',
'4':'0100',
'5':'0101',
'6':'0110',
'7':'0111',
'8':'1000',
'9':'1001',
'A':'1010',
'B':'1011',
'C':'1100',
'D':'1101',
'E':'1110',
'F':'1111'}

data = ll[0]
data = "".join([parse[x] for x in data])
print(len(data))

sumofversions=0
def parse(data):
    global sumofversions
    version = int(data[:3],2)
    sumofversions+=version
    data=data[3:]

    tid = int(data[:3],2)
    data=data[3:]
    if tid == 4:
        t = ""
        while True:
            t += data[1:5]
            cnt = data[0]
            data=data[5:]
            if cnt == '0':
                break
    else:
        ltid= data[0]
        data=data[1:]
        if ltid == '0':
            l = data[:15]
            data=data[15:]
            subpacketslen = int(l, 2)
            subpackets = data[:subpacketslen]
            while subpackets:
                subpackets = parse(subpackets)
            data=data[subpacketslen:]
        else:
            l = data[:11]
            data=data[11:]
            subpacketsqty = int(l, 2)
            for i in range(subpacketsqty):
                data=parse(data)
    return data

parse(data)
print(sumofversions)