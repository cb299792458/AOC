input = [l[:-1] for l in open('input.txt','r').readlines()]

class Node:
    def __init__(self, color, children):
        self.color = color
        self.children = children

nodes = dict()

for line in input:
    [parent, rest] = line.split(' bags contain ')
    children = dict()

    if rest == 'no other bags.':
        pass
    else:
        leaves = rest.split(', ')
        for leaf in leaves:
            [num, c1, c2, _] = leaf.split(' ')
            num = int(num)
            color = c1 + ' ' + c2
            children[color] = num
    
    nodes[parent] = Node(parent, children)

colors = nodes.keys()
def has_shiny_gold_as_child(node):
    if node.color == 'shiny gold':
        return True # must subtract 1 at end
    for child in node.children.keys():
        if has_shiny_gold_as_child(nodes[child]):
            return True
    
    return False

part1 = 0
for color in colors:
    if has_shiny_gold_as_child(nodes[color]):
        part1 += 1
print(part1)

def count_children(color):
    total = 1
    node = nodes[color]

    for [child_color, num] in node.children.items():
        total += num * count_children(child_color)
    
    return total

print(count_children('shiny gold')) # subtract 1 again for shiny gold


