input = [l[:-1] for l in open('input.txt','r').readlines()]

closure = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

pt2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

score = 0
scores = []
for line in input:
    stack = []
    curr = 0

    incomplete = True
    for c in line:
        if c in closure.keys():
            stack.append(c)
        else:
            if c==closure[stack[-1]]:
                stack.pop()
            else:
                score += points[c]
                incomplete = False
                break
    
    if not incomplete:
        continue
    
    for c in stack[::-1]:
        curr *= 5
        curr += pt2[c]
    scores.append(curr)
    
print(score)

scores.sort()
print(scores[len(scores)//2])