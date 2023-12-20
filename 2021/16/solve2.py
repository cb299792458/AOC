input = [l[:-1] for l in open('input.txt','r').readlines()]
input = input[0]

binary = ''
for c in input:
    part = bin(int(c,16))[2:]
    binary += '0'*(4-len(part)) + part

def parse(binary):
    version = int(binary[:3],2)
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
        return [int(lit_val,2),binary]
    else:
        length_type_id = binary[0]
        binary = binary[1:]
        subvalues = []

        if length_type_id=='0':
            length = int(binary[:15],2)
            binary = binary[15:]
            subpackets = binary[:length]

            while subpackets:
                [value, new_subpackets] = parse(subpackets)
                subvalues.append(value)
                subpackets = new_subpackets
            binary = binary[length:]
        else:
            num_subpackets = int(binary[:11],2)
            binary = binary[11:]
            for _ in range(num_subpackets):
                [value, new_binary] = parse(binary)   
                subvalues.append(value)
                binary = new_binary

        match type:
            case 0:
                return [sum(subvalues), binary]
            case 1:
                product = 1
                for val in subvalues:
                    product *= val
                return [product, binary]
            case 2:
                return [min(subvalues), binary]
            case 3:
                return [max(subvalues), binary]
            case 5:
                return [1 if subvalues[0]>subvalues[1] else 0, binary]
            case 6:
                return [1 if subvalues[0]<subvalues[1] else 0, binary]
            case 7:
                return [1 if subvalues[0]==subvalues[1] else 0, binary]
            case _:
                print('uhoh')

print(parse(binary))
