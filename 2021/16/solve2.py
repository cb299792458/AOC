input = [l[:-1] for l in open('input.txt','r').readlines()][0]

def binarize(hex):
    binary = bin(int(hex,16))[2:]
    while len(binary)%4:
        binary = '0' + binary
    return binary

def parse(binary):
    versions = 0
    stack = []
    processed = []

    version = None
    type_id = None
    lit_str = ''
    length_type_id = None
    length = None
    num_subpackets = None
    subpackets = []

    for i,c in enumerate(binary):
        stack.append(c)

        if not version and len(stack)==3:
            version = int(''.join(stack),2)
            versions += version
            print(version, binary[i-2:])
            stack = []
        if not type_id and len(stack)==3:
            type_id = int(''.join(stack),2)
            stack = []

        if type_id==4 and len(stack)==5:
            group = ''.join(stack)
            lit_str += group[1:]
            stack = []

            if group[0]=='0':
                if length or num_subpackets:
                    subpackets.append((version,type_id,int(lit_str,2)))
                    if num_subpackets:
                        num_subpackets -= 1
                else:
                    processed.append((version,type_id,int(lit_str,2)))
                version = None
                type_id = None
                lit_str = ''

        if type_id and type_id!=4 and not length_type_id and len(stack)==1:
            length_type_id = stack[0]
            stack = []

        if type_id and type_id!=4 and length_type_id=='0' and len(stack)==15:
            length = int(''.join(stack),2) + 1 # +1 for current
            stack = []
            version, type_id = None, None
            length_type_id = None

        if type_id and type_id!=4 and length_type_id=='1' and len(stack)==11:
            num_subpackets = int(''.join(stack),2)
            stack = []
            version, type_id = None, None
            length_type_id = None

        if length:
            length -= 1

        if length==0 or num_subpackets==0:
            processed.append(subpackets)
            version, type_id = None, None
            length=None
            num_subpackets=None
            subpackets=[]

    print(processed, stack, subpackets, versions)
    return processed

# parse(binarize('D2FE28'))
# parse(binarize('38006F45291200'))
# parse(binarize('EE00D40C823060'))

# parse(binarize('8A004A801A8002F478'))
parse(binarize('620080001611562C8802118E34'))
# parse(binarize('C0015000016115A2E0802F182340'))
# parse(binarize('A0016C880162017C3686B18A3D4780'))
