input = [l[:-1] for l in open('input.txt','r').readlines()]
input = input[0]

versions = 0

def parse(string):
    # print(string)

    binary = bin(int(string,16))[2:]
    while len(binary)%4:
        binary = '0' + binary
    print(binary)
    # print(len(binary))

    version = int(binary[:3],2)
    global versions
    versions += version
    # print('version:',version)
    type = int(binary[3:6],2)
    # print(version,type)

    binary = binary[6:]
    if type==4:
        literal, remainder, lost_length = type4(binary)
        print(literal)
        if not all(c=='0' for c in remainder):
            parse(remainder)

    else:
        packet_vals, remainder, lost_length = packets(binary)
        print(packet_vals, remainder)

def type4(binary):
    print('4', binary)
    orig = len(binary)
    val=''
    while binary[0]!='0':
        val += binary[1:5]
        binary = binary[5:]
    val += binary[1:5]
    binary = binary[5:]

    print('lost', orig-len(binary))
    return (int(val,2), binary, orig-len(binary))

def packets(binary):
    print(binary)
    orig = len(binary)

    res = []
    id = binary[0]

    if id=='0':
        length = int(binary[1:16],2)
        while length:
            print(length)
            version = int(binary[16:19],2)
            type = int(binary[19:22],2)

            if type==4:
                val, remainder, lost_length = type4(binary[16:])
                res.append(val)

                length -= lost_length
                binary = remainder

            else:
                sub_vals, remainder, lost_length = packets(binary[22:])
                res += sub_vals

                length -= lost_length
                binary = remainder
            # print(length)

    # elif num:
    #     while num:
    #         version = int(binary[:3],2)
    #         type = int(binary[3:6],2)

    #         if type==4:
    #             val, remainder = type4(binary[6:])
    #             res.append(val)

    #             if all(c=='0' for c in remainder):
    #                 num=0
    #                 binary=''
    #             else:
    #                 num -= 1
    #                 binary = remainder


    return res, binary, orig-len(binary)

# parse('D2FE28')
parse('38006F45291200')
# parse('EE00D40C823060')
            
# parse('620080001611562C8802118E34')
# parse('C0015000016115A2E0802F182340')

# print(versions)