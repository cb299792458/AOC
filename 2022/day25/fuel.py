input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

digit = {
    '2':2,'1':1,'0':0,'-':-1,'=':-2,
}
def snafu_to_dec(str):
    chars = [c for c in str][::-1]
    power=sum=0
    
    for c in chars:
        sum += (5**power)*digit[c]
        power+=1
    
    return sum

total=sum([snafu_to_dec(line) for line in input])
print(total)

def dec_to_snafu(num):
    chars=[]

    while num:
        last_digit = num % 5
        if last_digit > 2:
            last_digit-=5
            num+=5
    
        if last_digit>-1:
            chars.append(str(last_digit))
        elif last_digit==-2:
            chars.append('=')
        elif last_digit==-1:
            chars.append('-')

        num=num//5

    return ''.join(chars[::-1])

print(dec_to_snafu(total))
