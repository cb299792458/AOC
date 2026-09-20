from collections import deque
input = [l[:-1] for l in open('input.txt','r').readlines()]
# 1 + (2 * 3) + (4 * (5 + 6))

def evaluate(string): # 1 + (2 * 3) + (4 * (5 + 6))

    # handle parentheses
    stack = []
    for char in string:
        if char == ')':
            substring = deque()
            while stack[-1] != '(':
                substring.appendleft(stack.pop())

            stack.pop()
            stack.append(str(evaluate(''.join(substring))))

        else:
            stack.append(char)

    # the magic line that combines separate strings digits into full string numbers
    # e.g. ['1', '2'] -> ['12']
    stack = ''.join(stack).split(' ')

    # handle math
    res = 0

    operation = '+'
    for char in stack:
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