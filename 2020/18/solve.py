input = [l[:-1] for l in open('input.txt','r').readlines()]
# 1 + (2 * 3) + (4 * (5 + 6))

def evaluate(string): # 1 + (2 * 3) + (4 * (5 + 6))
    # handle parentheses
    stack = []
    for char in string:
        if char == ')':
            substring = ''
            while stack[-1] != '(':
                substring = str(stack.pop()) + substring

            stack.pop()
            stack.append(str(evaluate(substring)))

        else:
            stack.append(char)

    # the magic line that combines separate strings digits into full string numbers
    # e.g. ['1', '2'] -> ['12']
    stack = ''.join(stack).split(' ')

    # handle math
    res = int(stack[0])

    operation = ''
    for char in stack[1:]:
        if char == ' ':
            continue
        if char in '+-*':
            operation = char

        else:
            match operation:
                case '+':
                    res += int(char)
                case '-':
                    res -= int(char)
                case '*':
                    res *= int(char)
                case _:
                    raise 'unknown operation'
    return res

print(sum([evaluate(line) for line in input]))