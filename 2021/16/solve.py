input = [l[:-1] for l in open('input.txt','r').readlines()]
input = input[0]

versions = 0

hex_to_bin = {
    '0':'0000',
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
    'F':'1111'
}
def binarize(hex):
    return ''.join([hex_to_bin[c] for c in hex])

def parse(binary):
    version = int(binary[:3],2)
    global versions
    versions += version

    type = int(binary[3:6],2)

    binary = binary[6:]
    if type==4:
        lit_val = ''
        while True:
            first = binary[0]
            lit_val += binary[1:5]
            binary=binary[5:]
            if first=='0':
                break
    else:
        length_type_id = binary[0]
        binary = binary[1:]

        if length_type_id=='0':
            length = int(binary[:15],2)
            binary = binary[15:]
            subpackets = binary[:length]

            while subpackets:
                subpackets = parse(subpackets)
            binary = binary[length:]
        else:
            num_subpackets = int(binary[:11],2)
            binary = binary[11:]
            for _ in range(num_subpackets):
                binary = parse(binary)
    return binary

parse(binarize(input))
print(versions)

# print(len(binarize(input)))